// SPDX-License-Identifier: MIT
// Copyright (c) 2018-2025, Advanced Micro Devices, Inc. All rights reserved.

#pragma once

#include <iostream>
#include <sstream>

#include "ck/library/utility/numeric.hpp"
#include "ck/utility/common_header.hpp"
#include "ck/utility/env.hpp"
#include "ck/tensor_description/tensor_descriptor.hpp"
#include "ck/tensor_description/tensor_descriptor_helper.hpp"
#include "ck/tensor_operation/gpu/device/tensor_layout.hpp"
#include "ck/tensor_operation/gpu/device/device_grouped_conv_bwd_data_multiple_d.hpp"
#include "ck/tensor_operation/gpu/device/convolution_backward_data_specialization.hpp"
#include "ck/tensor_operation/operator_transform/transform_conv_bwd_data_to_gemm_v1.hpp"
#include "ck/tensor_operation/gpu/grid/gridwise_gemm_xdl_cshuffle_conv_v3.hpp"
#include "ck/tensor_operation/gpu/device/gemm_specialization.hpp"
#include "ck/tensor_operation/operator_transform/transform_conv_ngchw_to_nhwgc.hpp"
#include "ck/tensor_operation/gpu/grid/gridwise_gemm_multiple_d_xdl_cshuffle.hpp"
#include "ck/tensor_operation/gpu/grid/gridwise_elementwise_2d.hpp"
#include "ck/tensor_operation/gpu/device/impl/device_grouped_conv_utils.hpp"
#include "ck/host_utility/device_prop.hpp"
#include "ck/host_utility/kernel_launch.hpp"
#include "ck/host_utility/flush_cache.hpp"
#include "ck/host_utility/io.hpp"

namespace ck {
namespace tensor_operation {
namespace device {

namespace {

/*
 * \brief Wrapper function of GridwiseGemm::Run to realize BatchedGEMM.
 *
 * \tparam ComputePtrOffsetOfBatch Class that computes the base pointer offsets of A, B, C matrix
 * given the batch. For example, ComputePtrOffsetOfStridedBatch() computes the offsets of evenly
 * strided batched, but we can easily extend to other layouts. The returned offset can be either \p
 * index_t or \p long_index_t. If it returns \p long_index_t, we are not subject to the 2GB
 * limitations.
 *
 * \tparam Block2ETileMap Block2ETileMap::CalculateBottomIndex() takes in id of a workgroup and
 * returns the 2D index of the tile that it computes. \see
 * GridwiseGemm_k0mk1_k0nk1_mn_xdlops_v2r3::Run().
 *
 * \note Using \p ComputePtrOffsetOfBatch gives us the flexibility that 2 workgroups can compute 2
 * tiles from different matrices. Keep in mind that these 2 matrices can share the same grid
 * descriptor (like in BatchedGEMM), or use their own grid descriptors (in GroupedGemm). \link
 * device_conv3d_fwd_xdl_ndhwc_kzyxc_ndhwk.hpp kernel_gemm_xdlops_v2r3_for_conv3d \endlink for \link
 * DeviceConv3d \endlink uses the same concept, but currently does NOT encapsulate the computing of
 * pointer offset into \p ComputePtrOffsetOfStridedBatch.
 *
 * \note \p Block2ETileMap allows customized mapping between a workgroup and the C-tile it computes.
 * Together with \p ComputePtrOffsetOfBatch, we can reuse GridwiseGemm (and GridwiseGemm fusion ) to
 * realize BatchedGemm and GroupedGemm (and the corresponding GEMM fusion).
 *
 */
template <typename GridwiseGemm,
          typename ABDataType,
          typename DsPointer,
          typename EDataType,
          typename AElementwiseOp,
          typename BElementwiseOp,
          typename CDEElementwiseOp,
          typename AGridDesc_AK0_M_AK1,
          typename BGridDesc_BK0_N_BK1,
          typename DsGridDescriptor_MBlock_MPerBlock_NBlock_NPerBlock,
          typename EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
          typename Block2ETileMap,
          typename ComputePtrOffsetOfBatch,
          typename ComputePtrOffsetOfN,
          bool HasMainKBlockLoop>
__global__ void
#if CK_USE_LAUNCH_BOUNDS
    __launch_bounds__(CK_MAX_THREAD_PER_BLOCK, CK_MIN_BLOCK_PER_CU)
#endif
        kernel_grouped_conv_bwd_data_multiple_d_xdl_cshuffle(
            const ABDataType* __restrict__ p_a_grid,
            const ABDataType* __restrict__ p_b_grid,
            DsPointer p_ds_grid,
            EDataType* __restrict__ p_e_grid,
            const AElementwiseOp a_element_op,
            const BElementwiseOp b_element_op,
            const CDEElementwiseOp cde_element_op,
            const AGridDesc_AK0_M_AK1 a_grid_desc_ak0_m_ak1,
            const BGridDesc_BK0_N_BK1 b_grid_desc_bk0_n_bk1,
            const DsGridDescriptor_MBlock_MPerBlock_NBlock_NPerBlock
                ds_grid_desc_mblock_mperblock_nblock_nperblock,
            const EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock
                e_grid_desc_mblock_mperblock_nblock_nperblock_,
            const Block2ETileMap block_2_ctile_map,
            const ComputePtrOffsetOfBatch compute_ptr_offset_of_batch,
            const ComputePtrOffsetOfN compute_ptr_offset_of_n)
{
#if(!defined(__HIP_DEVICE_COMPILE__) || defined(__gfx9__))
    // offset base pointer for each work-group
    const index_t n_idx = __builtin_amdgcn_readfirstlane(blockIdx.z);
    const index_t g_idx = __builtin_amdgcn_readfirstlane(blockIdx.y);

    const long_index_t a_batch_offset =
        amd_wave_read_first_lane(compute_ptr_offset_of_batch.GetAPtrOffset(g_idx));
    const long_index_t b_batch_offset =
        amd_wave_read_first_lane(compute_ptr_offset_of_batch.GetBPtrOffset(g_idx));
    const long_index_t e_batch_offset =
        amd_wave_read_first_lane(compute_ptr_offset_of_batch.GetEPtrOffset(g_idx));

    const auto ds_batch_offset = compute_ptr_offset_of_batch.GetDsPtrOffset(g_idx);

    const long_index_t a_n_offset =
        amd_wave_read_first_lane(compute_ptr_offset_of_n.GetAPtrOffset(n_idx));
    const long_index_t e_n_offset =
        amd_wave_read_first_lane(compute_ptr_offset_of_n.GetEPtrOffset(n_idx));

    __shared__ char p_shared[GridwiseGemm::GetSharedMemoryNumberOfByte()];

    DsPointer p_ds_grid_grp;

    static constexpr index_t NumDTensor =
        DsGridDescriptor_MBlock_MPerBlock_NBlock_NPerBlock::Size();

    static_for<0, NumDTensor, 1>{}(
        [&](auto i) { p_ds_grid_grp(i) = p_ds_grid[i] + ds_batch_offset[i]; });

    GridwiseGemm::template Run<HasMainKBlockLoop>(p_a_grid + a_batch_offset + a_n_offset,
                                                  p_b_grid + b_batch_offset,
                                                  p_ds_grid_grp,
                                                  p_e_grid + e_batch_offset + e_n_offset,
                                                  p_shared,
                                                  a_element_op,
                                                  b_element_op,
                                                  cde_element_op,
                                                  a_grid_desc_ak0_m_ak1,
                                                  b_grid_desc_bk0_n_bk1,
                                                  ds_grid_desc_mblock_mperblock_nblock_nperblock,
                                                  e_grid_desc_mblock_mperblock_nblock_nperblock_,
                                                  block_2_ctile_map);
#else
    ignore = p_a_grid;
    ignore = p_b_grid;
    ignore = p_ds_grid;
    ignore = p_e_grid;
    ignore = a_grid_desc_ak0_m_ak1;
    ignore = b_grid_desc_bk0_n_bk1;
    ignore = ds_grid_desc_mblock_mperblock_nblock_nperblock;
    ignore = e_grid_desc_mblock_mperblock_nblock_nperblock_;
    ignore = a_element_op;
    ignore = b_element_op;
    ignore = cde_element_op;
    ignore = compute_ptr_offset_of_batch;
    ignore = compute_ptr_offset_of_n;
    ignore = block_2_ctile_map;
#endif
}

template <typename GridwiseGemm,
          typename AGridDesc_AK0_M_K1,
          typename BGridDesc_BK0_N_K1,
          typename CGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
          typename ComputePtrOffsetOfBatch,
          typename ComputePtrOffsetOfN,
          bool HasMainKBlockLoop,
          InMemoryDataOperationEnum CGlobalMemoryDataOperation,
          index_t MinimumOccupancy = 1,
          TailNumber TailNum       = TailNumber::Full>
__global__ void
#if CK_USE_LAUNCH_BOUNDS
    __launch_bounds__(CK_MAX_THREAD_PER_BLOCK, MinimumOccupancy)
#endif
    // __attribute__((amdgpu_waves_per_eu(1, 1)))
    kernel_grouped_conv_bwd_data_xdl_cshuffle_v3(
        typename GridwiseGemm::Argument karg,
        const AGridDesc_AK0_M_K1 a_grid_desc_ak0_m_ak1,
        const BGridDesc_BK0_N_K1 b_grid_desc_bk0_n_bk1,
        const CGridDesc_MBlock_MPerBlock_NBlock_NPerBlock
            c_grid_desc_mblock_mperblock_nblock_nperblock,
        const ComputePtrOffsetOfBatch compute_ptr_offset_of_batch,
        const ComputePtrOffsetOfN compute_ptr_offset_of_n,
        const index_t num_k_per_block)
{
#if(!defined(__HIP_DEVICE_COMPILE__) || defined(__gfx908__) || defined(__gfx90a__) || \
    defined(__gfx940__) || defined(__gfx941__) || defined(__gfx942__))
    // offset base pointer for each work-group
    const index_t g_idx = __builtin_amdgcn_readfirstlane(blockIdx.z);
    const index_t n_idx = __builtin_amdgcn_readfirstlane(blockIdx.y / karg.KBatch);
    const index_t k_idx =
        __builtin_amdgcn_readfirstlane((blockIdx.y - n_idx * karg.KBatch) * num_k_per_block);

    const long_index_t a_batch_offset = __builtin_amdgcn_readfirstlane(
        static_cast<long_index_t>(compute_ptr_offset_of_batch.GetAPtrOffset(g_idx)));
    const long_index_t b_batch_offset = __builtin_amdgcn_readfirstlane(
        static_cast<long_index_t>(compute_ptr_offset_of_batch.GetBPtrOffset(g_idx)));
    const long_index_t e_batch_offset = __builtin_amdgcn_readfirstlane(
        static_cast<long_index_t>(compute_ptr_offset_of_batch.GetEPtrOffset(g_idx)));

    const long_index_t a_n_offset =
        amd_wave_read_first_lane(compute_ptr_offset_of_n.GetAPtrOffset(n_idx));
    const long_index_t e_n_offset =
        amd_wave_read_first_lane(compute_ptr_offset_of_n.GetEPtrOffset(n_idx));

    __shared__ char p_shared[GridwiseGemm::GetSharedMemoryNumberOfByte()];

    GridwiseGemm::template Run<AGridDesc_AK0_M_K1,
                               BGridDesc_BK0_N_K1,
                               CGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                               HasMainKBlockLoop,
                               CGlobalMemoryDataOperation,
                               TailNum>(karg.p_a_grid + a_batch_offset + a_n_offset,
                                        karg.p_b_grid + b_batch_offset,
                                        karg.p_c_grid + e_batch_offset + e_n_offset,
                                        p_shared,
                                        karg,
                                        a_grid_desc_ak0_m_ak1,
                                        b_grid_desc_bk0_n_bk1,
                                        c_grid_desc_mblock_mperblock_nblock_nperblock,
                                        k_idx);
#else
    ignore = karg;
    ignore = a_grid_desc_ak0_m_ak1;
    ignore = b_grid_desc_bk0_n_bk1;
    ignore = c_grid_desc_mblock_mperblock_nblock_nperblock;
    ignore = compute_ptr_offset_of_batch;
    ignore = compute_ptr_offset_of_n;
    ignore = num_k_per_block;
#endif // end of if (defined(__gfx908__) || defined(__gfx90a__))
}

template <typename GridwiseGemm,
          typename AGridDesc_AK0_M_K1,
          typename BGridDesc_BK0_N_K1,
          typename CGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
          typename ComputePtrOffsetOfBatch,
          typename ComputePtrOffsetOfN,
          bool HasMainKBlockLoop,
          InMemoryDataOperationEnum CGlobalMemoryDataOperation,
          index_t MinimumOccupancy = 1,
          TailNumber TailNum       = TailNumber::Full>
__global__ void
#if CK_USE_LAUNCH_BOUNDS
    __launch_bounds__(CK_MAX_THREAD_PER_BLOCK, MinimumOccupancy)
#endif
    // __attribute__((amdgpu_waves_per_eu(1, 1)))
    kernel_grouped_conv_bwd_data_xdl_cshuffle_v3_2lds(
        typename GridwiseGemm::Argument karg,
        const AGridDesc_AK0_M_K1 a_grid_desc_ak0_m_ak1,
        const BGridDesc_BK0_N_K1 b_grid_desc_bk0_n_bk1,
        const CGridDesc_MBlock_MPerBlock_NBlock_NPerBlock
            c_grid_desc_mblock_mperblock_nblock_nperblock,
        const ComputePtrOffsetOfBatch compute_ptr_offset_of_batch,
        const ComputePtrOffsetOfN compute_ptr_offset_of_n,
        const index_t num_k_per_block)
{
#if(!defined(__HIP_DEVICE_COMPILE__) || defined(__gfx908__) || defined(__gfx90a__) || \
    defined(__gfx940__) || defined(__gfx941__) || defined(__gfx942__))
    const index_t g_idx = __builtin_amdgcn_readfirstlane(blockIdx.z);
    const index_t n_idx = __builtin_amdgcn_readfirstlane(blockIdx.y / karg.KBatch);
    const index_t k_idx =
        __builtin_amdgcn_readfirstlane((blockIdx.y - n_idx * karg.KBatch) * num_k_per_block);

    const long_index_t a_batch_offset = __builtin_amdgcn_readfirstlane(
        static_cast<long_index_t>(compute_ptr_offset_of_batch.GetAPtrOffset(g_idx)));
    const long_index_t b_batch_offset = __builtin_amdgcn_readfirstlane(
        static_cast<long_index_t>(compute_ptr_offset_of_batch.GetBPtrOffset(g_idx)));
    const long_index_t e_batch_offset = __builtin_amdgcn_readfirstlane(
        static_cast<long_index_t>(compute_ptr_offset_of_batch.GetEPtrOffset(g_idx)));

    const long_index_t a_n_offset =
        amd_wave_read_first_lane(compute_ptr_offset_of_n.GetAPtrOffset(n_idx));
    const long_index_t e_n_offset =
        amd_wave_read_first_lane(compute_ptr_offset_of_n.GetEPtrOffset(n_idx));

    // Pass two lds pointer is the key to tell compiler that ds_read/write
    // operate on different lds chunk at same time without order dependecy
    __shared__ char p_shared_0[GridwiseGemm::GetSharedMemoryNumberOfByte()];
    __shared__ char p_shared_1[GridwiseGemm::GetSharedMemoryNumberOfByte()];

    GridwiseGemm::template Run_2Lds<AGridDesc_AK0_M_K1,
                                    BGridDesc_BK0_N_K1,
                                    CGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                    HasMainKBlockLoop,
                                    CGlobalMemoryDataOperation,
                                    TailNum>(karg.p_a_grid + a_batch_offset + a_n_offset,
                                             karg.p_b_grid + b_batch_offset,
                                             karg.p_c_grid + e_batch_offset + e_n_offset,
                                             p_shared_0,
                                             p_shared_1,
                                             karg,
                                             a_grid_desc_ak0_m_ak1,
                                             b_grid_desc_bk0_n_bk1,
                                             c_grid_desc_mblock_mperblock_nblock_nperblock,
                                             k_idx);
#else
    ignore = karg;
    ignore = a_grid_desc_ak0_m_ak1;
    ignore = b_grid_desc_bk0_n_bk1;
    ignore = c_grid_desc_mblock_mperblock_nblock_nperblock;
    ignore = compute_ptr_offset_of_batch;
    ignore = compute_ptr_offset_of_n;
    ignore = num_k_per_block;
#endif // end of if (defined(__gfx908__) || defined(__gfx90a__))
}

} // namespace

// Conv backward data multiple D:
//   input : output image A: [G, N, K, Ho, Wo]
//   input : weight B: [G, K, C, Y, X],
//   input : D0, D1, ... : [G, N, K, Ho, Wo]
//   output : input image E: [G, N, C, Hi, Wi]
//   C = a_op(A) * b_op(B)
//   E = cde_op(C, D0, D1, ...)
template <index_t NDimSpatial,
          typename ALayout,   // output image
          typename BLayout,   // weight
          typename DsLayout,  // bias
          typename ELayout,   // input image
          typename ADataType, // output image
          typename BDataType, // weight
          typename AccDataType,
          typename CShuffleDataType,
          typename DsDataType,       // bias
          typename EDataType,        // input image
          typename AElementwiseOp,   // output image
          typename BElementwiseOp,   // weight
          typename CDEElementwiseOp, // C, bias, and input image
          ConvolutionBackwardDataSpecialization ConvBackwardDataSpecialization,
          bool DoPadGemmM,
          bool DoPadGemmN,
          index_t NumGemmKPrefetchStage,
          index_t BlockSize,
          index_t MPerBlock,
          index_t NPerBlock,
          index_t KPerBlock,
          index_t AK1,
          index_t BK1,
          index_t MPerXDL,
          index_t NPerXDL,
          index_t MXdlPerWave,
          index_t NXdlPerWave,
          typename ABlockTransferThreadClusterLengths_AK0_M_AK1,
          typename ABlockTransferThreadClusterArrangeOrder,
          typename ABlockTransferSrcAccessOrder,
          index_t ABlockTransferSrcVectorDim,
          index_t ABlockTransferSrcScalarPerVector,
          index_t ABlockTransferDstScalarPerVector_AK1,
          index_t ABlockLdsExtraM,
          typename BBlockTransferThreadClusterLengths_BK0_N_BK1,
          typename BBlockTransferThreadClusterArrangeOrder,
          typename BBlockTransferSrcAccessOrder,
          index_t BBlockTransferSrcVectorDim,
          index_t BBlockTransferSrcScalarPerVector,
          index_t BBlockTransferDstScalarPerVector_BK1,
          index_t BBlockLdsExtraN,
          index_t CShuffleMXdlPerWavePerShuffle,
          index_t CShuffleNXdlPerWavePerShuffle,
          typename CDEBlockTransferClusterLengths_MBlock_MPerBlock_NBlock_NPerBlock,
          index_t CDEBlockTransferScalarPerVector_NPerBlock,
          LoopScheduler LoopSched                        = make_default_loop_scheduler(),
          typename AComputeType                          = ADataType,
          typename BComputeType                          = AComputeType,
          index_t MaxTransposeTransferInScalarPerVector  = 1,
          index_t MaxTransposeTransferOutScalarPerVector = 1,
          BlockGemmPipelineScheduler BlkGemmPipeSched    = BlockGemmPipelineScheduler::Intrawave,
          BlockGemmPipelineVersion BlkGemmPipelineVer    = BlockGemmPipelineVersion::v1>
struct DeviceGroupedConvBwdDataMultipleD_Xdl_CShuffle_v1
    : public DeviceGroupedConvBwdDataMultipleD<NDimSpatial,
                                               ALayout,    // output image
                                               BLayout,    // weight
                                               DsLayout,   // bias
                                               ELayout,    // input image
                                               ADataType,  // output image
                                               BDataType,  // weight
                                               DsDataType, // bias
                                               EDataType,  // input image
                                               AElementwiseOp,
                                               BElementwiseOp,
                                               CDEElementwiseOp,
                                               AComputeType,
                                               BComputeType>
{
    // TODO: Extend support for more spatial dimensions.
    static_assert(NDimSpatial == 2 || NDimSpatial == 3,
                  "wrong! only implemented for 2D and 3D now");

    using DeviceOp = DeviceGroupedConvBwdDataMultipleD_Xdl_CShuffle_v1;

    static constexpr index_t NumDTensor          = DsDataType::Size();
    static constexpr bool isMultiD               = NumDTensor > 0;
    static constexpr GemmSpecialization GemmSpec = GemmSpecialization::MNKPadding;
    static constexpr bool IsSplitKSupported =
        (CDEBlockTransferScalarPerVector_NPerBlock % 2 == 0 || sizeof(EDataType) % 4 == 0) &&
        std::is_same_v<remove_cvref_t<CDEElementwiseOp>, element_wise::PassThrough>;

    // TODO: Add support for different A and B data types.
    using ABDataType = ADataType;

    static constexpr auto I0 = Number<0>{};
    static constexpr auto I1 = Number<1>{};
    static constexpr auto I2 = Number<2>{};
    static constexpr auto I3 = Number<3>{};

    using ALayoutAfterTranspose =
        std::conditional_t<is_NGCHW_NGKHW<ELayout, BLayout, ALayout>(),
                           tensor_layout::convolution::NHWGK,
                           std::conditional_t<is_NGCDHW_NGKDHW<ELayout, BLayout, ALayout>(),
                                              tensor_layout::convolution::NDHWGK,
                                              ALayout>>;
    using BLayoutAfterTranspose =
        std::conditional_t<is_NGCHW_GKCYX_NGKHW<ELayout, BLayout, ALayout>(),
                           tensor_layout::convolution::GKYXC,
                           std::conditional_t<is_NGCDHW_GKCZYX_NGKDHW<ELayout, BLayout, ALayout>(),
                                              tensor_layout::convolution::GKZYXC,
                                              BLayout>>;
    using ELayoutAfterTranspose =
        std::conditional_t<is_NGCHW_NGKHW<ELayout, BLayout, ALayout>(),
                           tensor_layout::convolution::NHWGC,
                           std::conditional_t<is_NGCDHW_NGKDHW<ELayout, BLayout, ALayout>(),
                                              tensor_layout::convolution::NDHWGC,
                                              ELayout>>;

    using ConvToGemmBwdDataTransform = TransformConvBwdDataToGemm_v1<NDimSpatial,
                                                                     ConvBackwardDataSpecialization,
                                                                     AK1,
                                                                     BK1,
                                                                     MPerBlock,
                                                                     NPerBlock,
                                                                     KPerBlock,
                                                                     DoPadGemmM,
                                                                     DoPadGemmN,
                                                                     ALayoutAfterTranspose,
                                                                     BLayoutAfterTranspose,
                                                                     ELayoutAfterTranspose,
                                                                     true, /*SplitConvN*/
                                                                     ABDataType,
                                                                     EDataType>;

    static auto
    GetDummyABDsEGridDescriptor(const ConvToGemmBwdDataTransform& conv_to_gemm_transform)
    {
        const auto a_grid_desc_ak0_m_ak1 = conv_to_gemm_transform.MakeADescriptor_AK0_M_AK1();

        const auto b_grid_desc_bk0_n_bk1 = conv_to_gemm_transform.MakeBDescriptor_BK0_N_BK1();

        const auto ds_grid_desc_m_n = generate_tuple(
            [&](auto i) {
                using DLayout   = remove_cvref_t<tuple_element_t<i.value, DsLayout>>;
                using DDataType = remove_cvref_t<tuple_element_t<i.value, DsDataType>>;
                using ConvToGemmBwdDataTransformD =
                    TransformConvBwdDataToGemm_v1<NDimSpatial,
                                                  ConvBackwardDataSpecialization,
                                                  AK1,
                                                  BK1,
                                                  MPerBlock,
                                                  NPerBlock,
                                                  KPerBlock,
                                                  DoPadGemmM,
                                                  DoPadGemmN,
                                                  ALayoutAfterTranspose,
                                                  BLayout,
                                                  DLayout,
                                                  true, /*SplitConvN*/
                                                  ABDataType,
                                                  DDataType>;
                return ConvToGemmBwdDataTransformD{}.MakeCDescriptor_M_N();
            },
            Number<NumDTensor>{});

        const auto e_grid_desc_m_n = conv_to_gemm_transform.MakeCDescriptor_M_N();

        return make_tuple(
            a_grid_desc_ak0_m_ak1, b_grid_desc_bk0_n_bk1, ds_grid_desc_m_n, e_grid_desc_m_n);
    }

// GridwiseGemm
#define GridwiseGemmMultiDTemplateParams                                                        \
    ABDataType, ABDataType, AComputeType, AccDataType, CShuffleDataType, DsDataType, EDataType, \
        AElementwiseOp, BElementwiseOp, CDEElementwiseOp, InMemoryDataOperationEnum::Set,       \
        NumGemmKPrefetchStage, BlockSize, MPerBlock, NPerBlock, KPerBlock, AK1, BK1, MPerXDL,   \
        NPerXDL, MXdlPerWave, NXdlPerWave, ABlockTransferThreadClusterLengths_AK0_M_AK1,        \
        ABlockTransferThreadClusterArrangeOrder, ABlockTransferSrcAccessOrder,                  \
        ABlockTransferSrcVectorDim, ABlockTransferSrcScalarPerVector,                           \
        ABlockTransferDstScalarPerVector_AK1, false, ABlockLdsExtraM,                           \
        BBlockTransferThreadClusterLengths_BK0_N_BK1, BBlockTransferThreadClusterArrangeOrder,  \
        BBlockTransferSrcAccessOrder, BBlockTransferSrcVectorDim,                               \
        BBlockTransferSrcScalarPerVector, BBlockTransferDstScalarPerVector_BK1, false,          \
        BBlockLdsExtraN, CShuffleMXdlPerWavePerShuffle, CShuffleNXdlPerWavePerShuffle,          \
        CDEBlockTransferClusterLengths_MBlock_MPerBlock_NBlock_NPerBlock,                       \
        CDEBlockTransferScalarPerVector_NPerBlock, LoopSched, PipelineVersion::v1, BComputeType

#define GridwiseGemmTemplateParams                                                               \
    tensor_layout::gemm::RowMajor, tensor_layout::gemm::RowMajor, tensor_layout::gemm::RowMajor, \
        ADataType, BDataType, AccDataType, CShuffleDataType, EDataType, AElementwiseOp,          \
        BElementwiseOp, CDEElementwiseOp, GemmSpec, BlockSize, MPerBlock, NPerBlock, KPerBlock,  \
        AK1, BK1, MPerXDL, NPerXDL, MXdlPerWave, NXdlPerWave,                                    \
        ABlockTransferThreadClusterLengths_AK0_M_AK1, ABlockTransferThreadClusterArrangeOrder,   \
        ABlockTransferSrcAccessOrder, ABlockTransferSrcVectorDim,                                \
        ABlockTransferSrcScalarPerVector, ABlockTransferDstScalarPerVector_AK1, false,           \
        ABlockLdsExtraM, BBlockTransferThreadClusterLengths_BK0_N_BK1,                           \
        BBlockTransferThreadClusterArrangeOrder, BBlockTransferSrcAccessOrder,                   \
        BBlockTransferSrcVectorDim, BBlockTransferSrcScalarPerVector,                            \
        BBlockTransferDstScalarPerVector_BK1, false, BBlockLdsExtraN,                            \
        CShuffleMXdlPerWavePerShuffle, CShuffleNXdlPerWavePerShuffle,                            \
        CDEBlockTransferClusterLengths_MBlock_MPerBlock_NBlock_NPerBlock,                        \
        CDEBlockTransferScalarPerVector_NPerBlock, BlkGemmPipeSched, BlkGemmPipelineVer,         \
        AComputeType, BComputeType

    using GridwiseGemm =
        std::conditional_t<isMultiD,
                           GridwiseGemmMultipleD_xdl_cshuffle<GridwiseGemmMultiDTemplateParams>,
                           GridwiseGemm_xdl_cshuffle_v3<GridwiseGemmTemplateParams>>;

    template <typename EGridDesc_M_N>
    static auto
    MakeEGridDescriptor_MBlock_MPerBlock_NBlock_NPerBlock(const EGridDesc_M_N e_grid_desc_m_n)
    {
        if constexpr(isMultiD)
        {
            return GridwiseGemm::MakeEGridDescriptor_MBlock_MPerBlock_NBlock_NPerBlock(
                e_grid_desc_m_n);
        }
        else
        {
            const index_t M = e_grid_desc_m_n.GetLength(I0);
            const index_t N = e_grid_desc_m_n.GetLength(I1);
            return GridwiseGemm::MakeCGridDescriptor_MBlock_MPerBlock_NBlock_NPerBlock(
                e_grid_desc_m_n,
                GridwiseGemm::CalculateMBlock(M),
                GridwiseGemm::CalculateNBlock(N));
        }
    }

    template <typename Desc_K0_M_K1>
    static auto transform_k0_m_k1_to_m_k(const Desc_K0_M_K1& desc_k0_m_k1)
    {
        const auto grid_desc_m_k = transform_tensor_descriptor(
            desc_k0_m_k1,
            make_tuple(make_pass_through_transform(desc_k0_m_k1.GetLength(I1)),
                       make_merge_transform(
                           make_tuple(desc_k0_m_k1.GetLength(I0), desc_k0_m_k1.GetLength(I2)))),
            make_tuple(Sequence<1>{}, Sequence<0, 2>{}),
            make_tuple(Sequence<0>{}, Sequence<1>{}));

        return grid_desc_m_k;
    }

    // desc
    constexpr static ConvToGemmBwdDataTransform dummy_conv_to_gemm_transform;
    using ABDsEGridDesc = decltype(GetDummyABDsEGridDescriptor(dummy_conv_to_gemm_transform));

    using AGridDesc_AK0_M_AK1 = remove_cvref_t<tuple_element_t<0, ABDsEGridDesc>>;
    using BGridDesc_BK0_N_BK1 = remove_cvref_t<tuple_element_t<1, ABDsEGridDesc>>;
    using DsGridDesc_M_N      = remove_cvref_t<tuple_element_t<2, ABDsEGridDesc>>;
    using EGridDesc_M_N       = remove_cvref_t<tuple_element_t<3, ABDsEGridDesc>>;

    using AGridDesc_M_K = decltype(transform_k0_m_k1_to_m_k(AGridDesc_AK0_M_AK1{}));
    using BGridDesc_N_K = decltype(transform_k0_m_k1_to_m_k(BGridDesc_BK0_N_BK1{}));

    using DsGridDesc_MBlock_MPerBlock_NBlock_NPerBlock =
        decltype(GridwiseGemmMultipleD_xdl_cshuffle<GridwiseGemmMultiDTemplateParams>::
                     MakeDsGridDescriptor_MBlock_MPerBlock_NBlock_NPerBlock(DsGridDesc_M_N{}));
    using EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock =
        decltype(MakeEGridDescriptor_MBlock_MPerBlock_NBlock_NPerBlock(EGridDesc_M_N{}));

    // block-to-e-tile map
    using Block2ETileMap = remove_cvref_t<
        decltype(GridwiseGemmMultipleD_xdl_cshuffle<
                 GridwiseGemmMultiDTemplateParams>::MakeDefaultBlock2ETileMap(EGridDesc_M_N{}))>;
    using Block2TileMapInOutElementwise = BlockToCTileMap_M00_N0_M01Adapt<NPerBlock, MPerBlock>;
    using Block2TileMapWeiElementwise   = BlockToCTileMap_M00_N0_M01Adapt<MPerBlock, NPerBlock>;

    static constexpr index_t ClusterLengthMPerBlock =
        CDEBlockTransferClusterLengths_MBlock_MPerBlock_NBlock_NPerBlock::At(1);
    static constexpr index_t ClusterLengthNPerBlock =
        CDEBlockTransferClusterLengths_MBlock_MPerBlock_NBlock_NPerBlock::At(3);

    static constexpr auto conv_ngchw_to_nhwgc_transformer =
        TransformConvNGCHWToNHWGC<ELayout,
                                  BLayout,
                                  ALayout,
                                  NDimSpatial,
                                  NPerBlock / ClusterLengthNPerBlock,
                                  MPerBlock / ClusterLengthMPerBlock>{};

    static constexpr index_t TransposeTransferInScalarPerVectorAligned =
        std::min(MPerBlock / ClusterLengthMPerBlock, MaxTransposeTransferInScalarPerVector);
    static constexpr index_t TransposeTransferOutScalarPerVectorAligned =
        std::min(MPerBlock / ClusterLengthMPerBlock, MaxTransposeTransferOutScalarPerVector);

    using NGCHWTransposeDescType =
        remove_cvref_t<decltype(conv_ngchw_to_nhwgc_transformer
                                    .template MakeNGCHWTransposeDesc<NDimSpatial>({}, {}))>;
    using NHWGCTransposeDescType =
        remove_cvref_t<decltype(conv_ngchw_to_nhwgc_transformer
                                    .template MakeNHWGCTransposeDesc<NDimSpatial>({}, {}))>;
    using GKCYXTransposeDescType =
        remove_cvref_t<decltype(conv_ngchw_to_nhwgc_transformer
                                    .template MakeGKCYXTransposeDesc<NDimSpatial>({}, {}))>;
    using GKYXCTransposeDescType =
        remove_cvref_t<decltype(conv_ngchw_to_nhwgc_transformer
                                    .template MakeGKYXCTransposeDesc<NDimSpatial>({}, {}))>;

    static constexpr index_t ElementwiseBlocksize = ClusterLengthMPerBlock * ClusterLengthNPerBlock;

    using GridwiseElementwiseInputTranspose =
        GridwiseElementwise<Tuple<NGCHWTransposeDescType>,
                            Tuple<NHWGCTransposeDescType>,
                            Tuple<const ADataType*>,
                            Tuple<ADataType*>,
                            Block2TileMapInOutElementwise,
                            element_wise::PassThrough,
                            ElementwiseBlocksize,
                            NPerBlock,
                            MPerBlock,
                            NPerBlock / ClusterLengthNPerBlock,
                            MPerBlock / ClusterLengthMPerBlock,
                            Sequence<1, 0>,
                            Sequence<TransposeTransferInScalarPerVectorAligned>,
                            Sequence<CDEBlockTransferScalarPerVector_NPerBlock>,
                            I1,
                            I0>;

    using GridwiseElementwiseWeightTranspose =
        GridwiseElementwise<Tuple<GKCYXTransposeDescType>,
                            Tuple<GKYXCTransposeDescType>,
                            Tuple<const BDataType*>,
                            Tuple<BDataType*>,
                            Block2TileMapWeiElementwise,
                            element_wise::PassThrough,
                            ElementwiseBlocksize,
                            MPerBlock,
                            NPerBlock,
                            MPerBlock / ClusterLengthMPerBlock,
                            NPerBlock / ClusterLengthNPerBlock,
                            Sequence<1, 0>,
                            Sequence<1>,
                            Sequence<CDEBlockTransferScalarPerVector_NPerBlock>,
                            I0,
                            I1>;

    using GridwiseElementwiseOutputTranspose =
        GridwiseElementwise<Tuple<NHWGCTransposeDescType>,
                            Tuple<NGCHWTransposeDescType>,
                            Tuple<const EDataType*>,
                            Tuple<EDataType*>,
                            Block2TileMapInOutElementwise,
                            element_wise::PassThrough,
                            ElementwiseBlocksize,
                            NPerBlock,
                            MPerBlock,
                            NPerBlock / ClusterLengthNPerBlock,
                            MPerBlock / ClusterLengthMPerBlock,
                            Sequence<1, 0>,
                            Sequence<CDEBlockTransferScalarPerVector_NPerBlock>,
                            Sequence<TransposeTransferOutScalarPerVectorAligned>,
                            I0,
                            I1>;
    // Argument
    struct Argument : public BaseArgument
    {
        Argument(const void* p_a,                                 // output image
                 const void* p_b,                                 // weight
                 const std::array<const void*, NumDTensor>& p_ds, // bias
                 void* p_e,                                       // input image
                 const std::array<index_t, NDimSpatial + 3>& a_g_n_k_wos_lengths,
                 const std::array<index_t, NDimSpatial + 3>& a_g_n_k_wos_strides,
                 const std::array<index_t, NDimSpatial + 3>& b_g_k_c_xs_lengths,
                 const std::array<index_t, NDimSpatial + 3>& b_g_k_c_xs_strides,
                 const std::array<std::array<index_t, NDimSpatial + 3>, NumDTensor>&
                     ds_g_n_c_wis_lengths,
                 const std::array<std::array<index_t, NDimSpatial + 3>, NumDTensor>&
                     ds_g_n_c_wis_strides,
                 const std::array<index_t, NDimSpatial + 3>& e_g_n_c_wis_lengths,
                 const std::array<index_t, NDimSpatial + 3>& e_g_n_c_wis_strides,
                 const std::array<index_t, NDimSpatial>& conv_filter_strides,
                 const std::array<index_t, NDimSpatial>& conv_filter_dilations,
                 const std::array<index_t, NDimSpatial>& input_left_pads,
                 const std::array<index_t, NDimSpatial>& input_right_pads,
                 const AElementwiseOp& a_element_op,
                 const BElementwiseOp& b_element_op,
                 const CDEElementwiseOp& cde_element_op,
                 ck::index_t split_k = 1)
            : p_a_grid_{static_cast<const ADataType*>(p_a)},
              p_b_grid_{static_cast<const BDataType*>(p_b)},
              p_ds_grid_{},
              p_e_grid_{static_cast<EDataType*>(p_e)},
              num_group_{a_g_n_k_wos_lengths[0]},
              a_element_op_{a_element_op},
              b_element_op_{b_element_op},
              cde_element_op_{cde_element_op},
              a_g_n_k_wos_lengths_{a_g_n_k_wos_lengths},
              b_g_k_c_xs_lengths_{b_g_k_c_xs_lengths},
              e_g_n_c_wis_lengths_{e_g_n_c_wis_lengths},
              conv_filter_strides_{conv_filter_strides},
              input_left_pads_{input_left_pads},
              input_right_pads_{input_right_pads},
              k_batch_{split_k}
        {
            std::array<index_t, NDimSpatial + 3> a_g_n_k_wos_strides_transposed =
                conv_ngchw_to_nhwgc_transformer.TransposeInOutStrides(a_g_n_k_wos_lengths,
                                                                      a_g_n_k_wos_strides);
            std::array<index_t, NDimSpatial + 3> b_g_k_c_xs_strides_transposed =
                conv_ngchw_to_nhwgc_transformer.TransposeWeiStrides(b_g_k_c_xs_lengths,
                                                                    b_g_k_c_xs_strides);
            std::array<index_t, NDimSpatial + 3> e_g_n_c_wis_strides_transposed =
                conv_ngchw_to_nhwgc_transformer.TransposeInOutStrides(e_g_n_c_wis_lengths,
                                                                      e_g_n_c_wis_strides);

            // populate Ds pointer
            static_for<0, NumDTensor, 1>{}([&](auto i) {
                using DDataType = remove_cvref_t<tuple_element_t<i.value, DsDataType>>;

                p_ds_grid_(i) = static_cast<const DDataType*>(p_ds[i]);
            });

            static_for<0, NumDTensor, 1>{}([&](auto i) {
                compute_ptr_offset_of_batch_.BatchStrideDs_(i) = ds_g_n_c_wis_strides[i][0];
            });

            static constexpr auto NonSpatialDimsNum = Number<3>{};

            static constexpr auto DIdx = Number<NonSpatialDimsNum>{};
            static constexpr auto HIdx =
                NDimSpatial == 2 ? Number<NonSpatialDimsNum>{} : Number<NonSpatialDimsNum + 1>{};
            static constexpr auto WIdx = NDimSpatial == 2 ? Number<NonSpatialDimsNum + 1>{}
                                                          : Number<NonSpatialDimsNum + 2>{};

            static constexpr auto ZIdx = Number<NonSpatialDimsNum>{};
            static constexpr auto YIdx =
                NDimSpatial == 2 ? Number<NonSpatialDimsNum>{} : Number<NonSpatialDimsNum + 1>{};
            static constexpr auto XIdx = NDimSpatial == 2 ? Number<NonSpatialDimsNum + 1>{}
                                                          : Number<NonSpatialDimsNum + 2>{};

            // problem definition
            const index_t Z = b_g_k_c_xs_lengths[ZIdx];
            const index_t Y = b_g_k_c_xs_lengths[YIdx];
            const index_t X = b_g_k_c_xs_lengths[XIdx];

            const index_t ConvStrideD = conv_filter_strides[DIdx - NonSpatialDimsNum];
            const index_t ConvStrideH = conv_filter_strides[HIdx - NonSpatialDimsNum];
            const index_t ConvStrideW = conv_filter_strides[WIdx - NonSpatialDimsNum];

            const index_t ConvDilationD = conv_filter_dilations[DIdx - NonSpatialDimsNum];
            const index_t ConvDilationH = conv_filter_dilations[HIdx - NonSpatialDimsNum];
            const index_t ConvDilationW = conv_filter_dilations[WIdx - NonSpatialDimsNum];

            const auto GcdStrideDilationD = math::gcd(ConvStrideD, ConvDilationD);
            const auto GcdStrideDilationH = math::gcd(ConvStrideH, ConvDilationH);
            const auto GcdStrideDilationW = math::gcd(ConvStrideW, ConvDilationW);

            const auto ZTilde = NDimSpatial == 3 ? ConvStrideD / GcdStrideDilationD : 1;
            const auto YTilde = ConvStrideH / GcdStrideDilationH;
            const auto XTilde = ConvStrideW / GcdStrideDilationW;

            for(index_t i_ztilde = 0; i_ztilde < ZTilde; ++i_ztilde)
            {

                for(index_t i_ytilde = 0; i_ytilde < YTilde; ++i_ytilde)
                {
                    for(index_t i_xtilde = 0; i_xtilde < XTilde; ++i_xtilde)
                    {
                        // check slice is valid
                        const auto ZDotSlice =
                            NDimSpatial == 3 ? math::integer_divide_ceil(Z - i_ztilde, ZTilde) : 1;
                        const auto YDotSlice = math::integer_divide_ceil(Y - i_ytilde, YTilde);
                        const auto XDotSlice = math::integer_divide_ceil(X - i_xtilde, XTilde);

                        if(YDotSlice * XDotSlice * ZDotSlice <= 0)
                        {
                            continue;
                        }

                        std::array<index_t, NDimSpatial> tildes;
                        if constexpr(NDimSpatial == 2)
                        {
                            tildes = {i_ytilde, i_xtilde};
                        }
                        else if constexpr(NDimSpatial == 3)
                        {
                            tildes = {i_ztilde, i_ytilde, i_xtilde};
                        }
                        else
                        {
                            throw std::runtime_error("wrong! only implemented for 2D and 3D now");
                        }

                        ConvToGemmBwdDataTransform conv_to_gemm_transform_{
                            a_g_n_k_wos_lengths,
                            a_g_n_k_wos_strides_transposed,
                            b_g_k_c_xs_lengths,
                            b_g_k_c_xs_strides_transposed,
                            e_g_n_c_wis_lengths,
                            e_g_n_c_wis_strides_transposed,
                            conv_filter_strides,
                            conv_filter_dilations,
                            input_left_pads,
                            input_right_pads,
                            tildes,
                            k_batch_};

                        conv_N_per_block_ = conv_to_gemm_transform_.N_;

                        const auto a_grid_desc_ak0_m_ak1 =
                            conv_to_gemm_transform_.MakeADescriptor_AK0_M_AK1();

                        const auto b_grid_desc_bk0_n_bk1 =
                            conv_to_gemm_transform_.MakeBDescriptor_BK0_N_BK1();

                        DsGridDesc_M_N ds_grid_desc_m_n;

                        // populate Ds desc
                        static_for<0, NumDTensor, 1>{}([&](auto i) {
                            using DLayout   = remove_cvref_t<tuple_element_t<i.value, DsLayout>>;
                            using DDataType = remove_cvref_t<tuple_element_t<i.value, DsDataType>>;
                            using ConvToGemmBwdDataTransformD =
                                TransformConvBwdDataToGemm_v1<NDimSpatial,
                                                              ConvBackwardDataSpecialization,
                                                              AK1,
                                                              BK1,
                                                              MPerBlock,
                                                              NPerBlock,
                                                              KPerBlock,
                                                              DoPadGemmM,
                                                              DoPadGemmN,
                                                              ALayoutAfterTranspose,
                                                              BLayoutAfterTranspose,
                                                              DLayout,
                                                              true, /*SplitConvN*/
                                                              ABDataType,
                                                              DDataType>;
                            ConvToGemmBwdDataTransformD conv_to_gemm_transform_d{
                                a_g_n_k_wos_lengths,
                                a_g_n_k_wos_strides_transposed,
                                b_g_k_c_xs_lengths,
                                b_g_k_c_xs_strides_transposed,
                                ds_g_n_c_wis_lengths[i],
                                ds_g_n_c_wis_strides[i],
                                conv_filter_strides,
                                conv_filter_dilations,
                                input_left_pads,
                                input_right_pads,
                                tildes};

                            ds_grid_desc_m_n(i) = conv_to_gemm_transform_d.MakeCDescriptor_M_N();
                        });

                        const auto e_grid_desc_m_n = conv_to_gemm_transform_.MakeCDescriptor_M_N();

                        // desc for problem definition
                        const auto a_grid_desc_m_k =
                            transform_k0_m_k1_to_m_k(a_grid_desc_ak0_m_ak1);
                        const auto b_grid_desc_n_k =
                            transform_k0_m_k1_to_m_k(b_grid_desc_bk0_n_bk1);

                        if constexpr(isMultiD)
                        {
                            a_grid_desc_m_k_container_.push_back(a_grid_desc_m_k);
                            b_grid_desc_n_k_container_.push_back(b_grid_desc_n_k);
                            ds_grid_desc_m_n_container_.push_back(ds_grid_desc_m_n);
                            e_grid_desc_m_n_container_.push_back(e_grid_desc_m_n);
                        }

                        // desc for blockwise copy
                        a_grid_desc_ak0_m_ak1_container_.push_back(a_grid_desc_ak0_m_ak1);
                        b_grid_desc_bk0_n_bk1_container_.push_back(b_grid_desc_bk0_n_bk1);

                        if constexpr(isMultiD)
                        {
                            // block-to-e-tile-map
                            auto block_2_etile_map =
                                GridwiseGemm::MakeDefaultBlock2ETileMap(e_grid_desc_m_n);

                            block_2_etile_map_container_.push_back(block_2_etile_map);

                            if(GridwiseGemm::CheckValidity(a_grid_desc_m_k,
                                                           b_grid_desc_n_k,
                                                           ds_grid_desc_m_n,
                                                           e_grid_desc_m_n,
                                                           block_2_etile_map))
                            {
                                ds_grid_desc_mblock_mperblock_nblock_nperblock_container_.push_back(

                                    GridwiseGemm::
                                        MakeDsGridDescriptor_MBlock_MPerBlock_NBlock_NPerBlock(
                                            ds_grid_desc_m_n));

                                e_grid_desc_mblock_mperblock_nblock_nperblock_container_.push_back(
                                    MakeEGridDescriptor_MBlock_MPerBlock_NBlock_NPerBlock(
                                        e_grid_desc_m_n));
                            }
                        }
                        else
                        {
                            // there is no need to check since M, N, K are padded
                            e_grid_desc_mblock_mperblock_nblock_nperblock_container_.push_back(
                                MakeEGridDescriptor_MBlock_MPerBlock_NBlock_NPerBlock(
                                    e_grid_desc_m_n));
                        }
                    }
                }
            }
            // A/B/Ds/E Batch Stride
            compute_ptr_offset_of_batch_.BatchStrideA_ = a_g_n_k_wos_strides_transposed[0];
            compute_ptr_offset_of_batch_.BatchStrideB_ = b_g_k_c_xs_strides_transposed[0];
            compute_ptr_offset_of_batch_.BatchStrideE_ = e_g_n_c_wis_strides_transposed[0];

            compute_ptr_offset_of_n_.BatchStrideA_ =
                a_g_n_k_wos_strides_transposed[1] * conv_N_per_block_;
            compute_ptr_offset_of_n_.BatchStrideE_ =
                e_g_n_c_wis_strides_transposed[1] * conv_N_per_block_;

            num_workgroups_per_Conv_N_ = a_g_n_k_wos_lengths_[I1] / conv_N_per_block_;

            if constexpr(is_NGCHW_NGKHW<ELayout, BLayout, ALayout>() ||
                         is_NGCDHW_NGKDHW<ELayout, BLayout, ALayout>())
            {
                // Use not modified base strides
                a_in_transpose_desc_ =
                    conv_ngchw_to_nhwgc_transformer.template MakeNGCHWTransposeDesc<NDimSpatial>(
                        a_g_n_k_wos_lengths, a_g_n_k_wos_strides, num_workgroups_per_Conv_N_);
                a_out_transpose_desc_ =
                    conv_ngchw_to_nhwgc_transformer.template MakeNHWGCTransposeDesc<NDimSpatial>(
                        a_g_n_k_wos_lengths, a_g_n_k_wos_strides, num_workgroups_per_Conv_N_);

                b_in_transpose_desc_ =
                    conv_ngchw_to_nhwgc_transformer.template MakeGKCYXTransposeDesc<NDimSpatial>(
                        b_g_k_c_xs_lengths, b_g_k_c_xs_strides);
                b_out_transpose_desc_ =
                    conv_ngchw_to_nhwgc_transformer.template MakeGKYXCTransposeDesc<NDimSpatial>(
                        b_g_k_c_xs_lengths, b_g_k_c_xs_strides);

                e_in_transpose_desc_ =
                    conv_ngchw_to_nhwgc_transformer.template MakeNHWGCTransposeDesc<NDimSpatial>(
                        e_g_n_c_wis_lengths, e_g_n_c_wis_strides, num_workgroups_per_Conv_N_);
                e_out_transpose_desc_ =
                    conv_ngchw_to_nhwgc_transformer.template MakeNGCHWTransposeDesc<NDimSpatial>(
                        e_g_n_c_wis_lengths, e_g_n_c_wis_strides, num_workgroups_per_Conv_N_);

                elementwise_block_2_ctile_map_transpose_a_ = Block2TileMapInOutElementwise{
                    a_in_transpose_desc_.GetLength(I0), a_in_transpose_desc_.GetLength(I1)};
                elementwise_block_2_ctile_map_transpose_b_ = Block2TileMapWeiElementwise{
                    b_in_transpose_desc_.GetLength(I0), b_in_transpose_desc_.GetLength(I1)};
                elementwise_block_2_ctile_map_transpose_e_ = Block2TileMapInOutElementwise{
                    e_in_transpose_desc_.GetLength(I0), e_in_transpose_desc_.GetLength(I1)};

                compute_ptr_offset_of_workspace_n_.BatchStrideA_ =
                    a_g_n_k_wos_strides[1] * conv_N_per_block_;
                compute_ptr_offset_of_workspace_n_.BatchStrideE_ =
                    e_g_n_c_wis_strides[1] * conv_N_per_block_;
            }
        }

        std::size_t GetWorkspaceATensorSizeBytes() const
        {
            if constexpr(is_NGCHW_NGKHW<ELayout, BLayout, ALayout>() ||
                         is_NGCDHW_NGKDHW<ELayout, BLayout, ALayout>())
            {
                const long_index_t a_acum = ck::accumulate_n<long_index_t>(
                    a_g_n_k_wos_lengths_.begin(), NDimSpatial + I3, 1, std::multiplies<>());
                // Align to 128B
                return math::integer_divide_ceil(sizeof(ADataType) * a_acum, 128) * 128;
            }
            else
            {
                return 0;
            }
        }

        std::size_t GetWorkspaceBTensorSizeBytes() const
        {
            if constexpr(is_NGCHW_GKCYX_NGKHW<ELayout, BLayout, ALayout>() ||
                         is_NGCDHW_GKCZYX_NGKDHW<ELayout, BLayout, ALayout>())
            {
                const long_index_t b_acum = ck::accumulate_n<long_index_t>(
                    b_g_k_c_xs_lengths_.begin(), NDimSpatial + I3, 1, std::multiplies<>());
                // Align to 128B
                return math::integer_divide_ceil(sizeof(BDataType) * b_acum, 128) * 128;
            }
            else
            {
                return 0;
            }
        }

        std::size_t GetWorkspaceETensorSizeBytes() const
        {
            if constexpr(is_NGCHW_NGKHW<ELayout, BLayout, ALayout>() ||
                         is_NGCDHW_NGKDHW<ELayout, BLayout, ALayout>())
            {
                const long_index_t e_accum = ck::accumulate_n<long_index_t>(
                    e_g_n_c_wis_lengths_.begin(), NDimSpatial + I3, 1, std::multiplies<>());
                return sizeof(EDataType) * e_accum;
            }
            else
            {
                return 0;
            }
        }

        std::size_t GetWorkspaceSizeBytes() const
        {
            return GetWorkspaceATensorSizeBytes() + GetWorkspaceBTensorSizeBytes() +
                   GetWorkspaceETensorSizeBytes();
        }

        void Print() const
        {
            for(std::size_t i = 0; i < a_grid_desc_ak0_m_ak1_container_.size(); i++)
            {
                std::cout << "a_grid_desc_ak0_m_ak1_container_"
                          << a_grid_desc_ak0_m_ak1_container_[i] << std::endl;

                std::cout << "b_grid_desc_bk0_n_bk1_container_"
                          << b_grid_desc_bk0_n_bk1_container_[i] << std::endl;

                static_for<0, NumDTensor, 1>{}([&](auto j) {
                    std::cout << "ds_grid_desc_mblock_mperblock_nblock_nperblock_container_"
                              << ds_grid_desc_mblock_mperblock_nblock_nperblock_container_[i][j]
                              << std::endl;
                });

                std::cout << "e_grid_desc_mblock_mperblock_nblock_nperblock_container_"
                          << e_grid_desc_mblock_mperblock_nblock_nperblock_container_[i]
                          << std::endl;
            }
        }

        // pointers
        const ADataType* p_a_grid_;
        const BDataType* p_b_grid_;
        typename GridwiseGemmMultipleD_xdl_cshuffle<GridwiseGemmMultiDTemplateParams>::DsGridPointer
            p_ds_grid_;
        EDataType* p_e_grid_;

        // tensor descriptor for problem definition
        index_t num_group_;
        index_t conv_N_per_block_;
        std::vector<AGridDesc_M_K> a_grid_desc_m_k_container_;
        std::vector<BGridDesc_N_K> b_grid_desc_n_k_container_;
        std::vector<DsGridDesc_M_N> ds_grid_desc_m_n_container_;
        std::vector<EGridDesc_M_N> e_grid_desc_m_n_container_;

        // tensor descriptor for block-wise copy
        std::vector<AGridDesc_AK0_M_AK1> a_grid_desc_ak0_m_ak1_container_;
        std::vector<BGridDesc_BK0_N_BK1> b_grid_desc_bk0_n_bk1_container_;
        std::vector<DsGridDesc_MBlock_MPerBlock_NBlock_NPerBlock>
            ds_grid_desc_mblock_mperblock_nblock_nperblock_container_;
        std::vector<EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock>
            e_grid_desc_mblock_mperblock_nblock_nperblock_container_;

        // block-to-e-tile map
        std::vector<Block2ETileMap> block_2_etile_map_container_;
        Block2TileMapInOutElementwise elementwise_block_2_ctile_map_transpose_a_,
            elementwise_block_2_ctile_map_transpose_e_;
        Block2TileMapWeiElementwise elementwise_block_2_ctile_map_transpose_b_;

        NGCHWTransposeDescType a_in_transpose_desc_, e_out_transpose_desc_;
        NHWGCTransposeDescType a_out_transpose_desc_, e_in_transpose_desc_;
        GKCYXTransposeDescType b_in_transpose_desc_;
        GKYXCTransposeDescType b_out_transpose_desc_;

        // for computing batch offset
        ComputePtrOffsetOfStridedBatch<I1, I1, NumDTensor> compute_ptr_offset_of_batch_;
        ComputePtrOffsetOfStridedBatch<I1, I1, I0> compute_ptr_offset_of_n_;
        ComputePtrOffsetOfStridedBatch<I1, I1, I0> compute_ptr_offset_of_workspace_n_;

        // element-wise op
        AElementwiseOp a_element_op_;
        BElementwiseOp b_element_op_;
        CDEElementwiseOp cde_element_op_;

        std::array<index_t, NDimSpatial + 3> a_g_n_k_wos_lengths_;
        std::array<index_t, NDimSpatial + 3> b_g_k_c_xs_lengths_;
        std::array<index_t, NDimSpatial + 3> e_g_n_c_wis_lengths_;
        std::array<index_t, NDimSpatial> conv_filter_strides_;
        std::array<index_t, NDimSpatial> input_left_pads_;
        std::array<index_t, NDimSpatial> input_right_pads_;

        const index_t k_batch_;
        index_t num_workgroups_per_Conv_N_;
    };

    // Invoker
    struct Invoker : public BaseInvoker
    {
        using Argument = DeviceOp::Argument;

        float RunMultiDGemm(const Argument& arg, const StreamConfig& stream_config = StreamConfig{})
        {
            float ave_time = 0;

            const index_t gdy = arg.num_group_;
            const index_t gdz = arg.num_workgroups_per_Conv_N_;

            const ADataType* p_a_grid = arg.p_a_grid_;
            const BDataType* p_b_grid = arg.p_b_grid_;
            EDataType* p_e_grid       = arg.p_e_grid_;

            if constexpr(is_NGCHW_NGKHW<ELayout, BLayout, ALayout>() ||
                         is_NGCDHW_NGKDHW<ELayout, BLayout, ALayout>())
            {
                p_a_grid = type_convert<const ADataType*>(arg.p_workspace_);
                p_e_grid =
                    type_convert<EDataType*>(arg.p_workspace_) +
                    (arg.GetWorkspaceATensorSizeBytes() + arg.GetWorkspaceBTensorSizeBytes()) /
                        sizeof(EDataType);
            }

            if constexpr(is_NGCHW_GKCYX_NGKHW<ELayout, BLayout, ALayout>() ||
                         is_NGCDHW_GKCZYX_NGKDHW<ELayout, BLayout, ALayout>())
            {
                p_b_grid = type_convert<const BDataType*>(arg.p_workspace_) +
                           arg.GetWorkspaceATensorSizeBytes() / sizeof(BDataType);
            }

            for(std::size_t i = 0; i < arg.a_grid_desc_ak0_m_ak1_container_.size(); i++)
            {
                if(!GridwiseGemm::CheckValidity(arg.a_grid_desc_m_k_container_[i],
                                                arg.b_grid_desc_n_k_container_[i],
                                                arg.ds_grid_desc_m_n_container_[i],
                                                arg.e_grid_desc_m_n_container_[i],
                                                arg.block_2_etile_map_container_[i]))
                {
                    throw std::runtime_error("wrong! device_op has invalid setting");
                }

                const index_t gdx = arg.block_2_etile_map_container_[i].CalculateGridSize(
                    arg.e_grid_desc_m_n_container_[i]);

                const auto GemmK = arg.a_grid_desc_m_k_container_[i].GetLength(I1);

                auto launch_kernel = [&](auto has_main_k_block_loop) {
                    constexpr bool has_main_loop = has_main_k_block_loop.value;

                    const auto kernel = kernel_grouped_conv_bwd_data_multiple_d_xdl_cshuffle<
                        GridwiseGemm,
                        ADataType, // TODO: distiguish A/B datatype
                        typename GridwiseGemm::DsGridPointer,
                        EDataType,
                        AElementwiseOp,
                        BElementwiseOp,
                        CDEElementwiseOp,
                        DeviceOp::AGridDesc_AK0_M_AK1,
                        DeviceOp::BGridDesc_BK0_N_BK1,
                        DeviceOp::DsGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                        DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                        Block2ETileMap,
                        ComputePtrOffsetOfStridedBatch<I1, I1, NumDTensor>,
                        ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                        has_main_loop>;

                    return launch_and_time_kernel(
                        stream_config,
                        kernel,
                        dim3(gdx, gdy, gdz),
                        dim3(BlockSize),
                        0,
                        p_a_grid,
                        p_b_grid,
                        arg.p_ds_grid_,
                        p_e_grid,
                        arg.a_element_op_,
                        arg.b_element_op_,
                        arg.cde_element_op_,
                        arg.a_grid_desc_ak0_m_ak1_container_[i],
                        arg.b_grid_desc_bk0_n_bk1_container_[i],
                        arg.ds_grid_desc_mblock_mperblock_nblock_nperblock_container_[i],
                        arg.e_grid_desc_mblock_mperblock_nblock_nperblock_container_[i],
                        arg.block_2_etile_map_container_[i],
                        arg.compute_ptr_offset_of_batch_,
                        arg.compute_ptr_offset_of_n_);
                };

                if(GridwiseGemm::CalculateHasMainKBlockLoop(GemmK))
                {
                    ave_time += launch_kernel(integral_constant<bool, true>{});
                }
                else
                {
                    ave_time += launch_kernel(integral_constant<bool, false>{});
                }
            }

            return ave_time;
        }

        float RunGemmV3(const Argument& arg, const StreamConfig& stream_config = StreamConfig{})
        {
            float ave_time = 0;

            const ADataType* p_a_grid = arg.p_a_grid_;
            const BDataType* p_b_grid = arg.p_b_grid_;
            EDataType* p_e_grid       = arg.p_e_grid_;

            if constexpr(is_NGCHW_NGKHW<ELayout, BLayout, ALayout>() ||
                         is_NGCDHW_NGKDHW<ELayout, BLayout, ALayout>())
            {
                p_a_grid = type_convert<const ADataType*>(arg.p_workspace_);
                p_e_grid =
                    type_convert<EDataType*>(arg.p_workspace_) +
                    (arg.GetWorkspaceATensorSizeBytes() + arg.GetWorkspaceBTensorSizeBytes()) /
                        sizeof(EDataType);
            }

            if constexpr(is_NGCHW_GKCYX_NGKHW<ELayout, BLayout, ALayout>() ||
                         is_NGCDHW_GKCZYX_NGKDHW<ELayout, BLayout, ALayout>())
            {
                p_b_grid = type_convert<const BDataType*>(arg.p_workspace_) +
                           arg.GetWorkspaceATensorSizeBytes() / sizeof(BDataType);
            }

            constexpr index_t minimum_occupancy =
                BlkGemmPipeSched == BlockGemmPipelineScheduler::Intrawave ? 1 : 2;

            for(std::size_t i = 0; i < arg.a_grid_desc_ak0_m_ak1_container_.size(); i++)
            {
                const index_t GemmM = arg.a_grid_desc_ak0_m_ak1_container_[i].GetLength(I1);
                const index_t GemmN = arg.b_grid_desc_bk0_n_bk1_container_[i].GetLength(I1);
                const index_t GemmK = arg.a_grid_desc_ak0_m_ak1_container_[i].GetLength(I0) *
                                      arg.a_grid_desc_ak0_m_ak1_container_[i].GetLength(I2);

                const auto num_k_per_block =
                    arg.a_grid_desc_ak0_m_ak1_container_[i].GetLength(Number<0>{}) / arg.k_batch_;

                // gdy is for the kbatch and num_workgrups_per_Conv_N
                index_t gdx, gdy, gdz;
                std::tie(gdx, gdy, gdz) = GridwiseGemm::CalculateGridSize(
                    GemmM, GemmN, arg.k_batch_ * arg.num_workgroups_per_Conv_N_, arg.num_group_);

                index_t k_grain = arg.k_batch_ * KPerBlock;
                index_t K_split = (GemmK + k_grain - 1) / k_grain * KPerBlock;
                const bool has_main_k_block_loop =
                    GridwiseGemm::CalculateHasMainKBlockLoop(K_split);

                typename GridwiseGemm::Argument gemm_arg{
                    p_a_grid, p_b_grid, p_e_grid, GemmM, GemmN, GemmK, I0, I0, I0, arg.k_batch_};

                const auto Run = [&](const auto& kernel) {
                    if(stream_config.flush_cache)
                    {
                        typename GridwiseGemm::Argument gemm_arg_ = gemm_arg;
                        ck::utility::RotatingMemWrapper<typename GridwiseGemm::Argument>
                            rotating_mem(gemm_arg_,
                                         stream_config.rotating_count,
                                         gemm_arg_.M * gemm_arg_.K * sizeof(ADataType),
                                         gemm_arg_.K * gemm_arg_.N * sizeof(BDataType));
                        rotating_mem.Print();

                        auto run_flush_cache = [&]() {
                            // flush icache
                            ck::utility::flush_icache();
                            // rotating mem
                            rotating_mem.Next();
                        };

                        ave_time += ck::utility::launch_and_time_kernel_with_preprocess<false>(
                            stream_config,
                            run_flush_cache,
                            kernel,
                            dim3(gdx, gdy, gdz),
                            dim3(BlockSize),
                            0,
                            gemm_arg_,
                            arg.a_grid_desc_ak0_m_ak1_container_[i],
                            arg.b_grid_desc_bk0_n_bk1_container_[i],
                            arg.e_grid_desc_mblock_mperblock_nblock_nperblock_container_[i],
                            arg.compute_ptr_offset_of_batch_,
                            arg.compute_ptr_offset_of_n_,
                            num_k_per_block);
                    }
                    else
                    {
                        ave_time += launch_and_time_kernel(
                            stream_config,
                            kernel,
                            dim3(gdx, gdy, gdz),
                            dim3(BlockSize),
                            0,
                            gemm_arg,
                            arg.a_grid_desc_ak0_m_ak1_container_[i],
                            arg.b_grid_desc_bk0_n_bk1_container_[i],
                            arg.e_grid_desc_mblock_mperblock_nblock_nperblock_container_[i],
                            arg.compute_ptr_offset_of_batch_,
                            arg.compute_ptr_offset_of_n_,
                            num_k_per_block);
                    }
                };

                if(has_main_k_block_loop)
                {
                    // Tail number always full
                    if constexpr(BlkGemmPipelineVer == BlockGemmPipelineVersion::v1 ||
                                 BlkGemmPipelineVer == BlockGemmPipelineVersion::v3)
                    {
                        if(gemm_arg.KBatch > 1)
                        {
                            if constexpr(IsSplitKSupported)
                            {
                                const auto kernel = kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                    GridwiseGemm,
                                    DeviceOp::AGridDesc_AK0_M_AK1,
                                    DeviceOp::BGridDesc_BK0_N_BK1,
                                    DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                    ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                    ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                    true,
                                    InMemoryDataOperationEnum::AtomicAdd,
                                    minimum_occupancy>;
                                Run(kernel);
                            }
                        }
                        else
                        {
                            const auto kernel = kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                GridwiseGemm,
                                DeviceOp::AGridDesc_AK0_M_AK1,
                                DeviceOp::BGridDesc_BK0_N_BK1,
                                DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                true,
                                InMemoryDataOperationEnum::Set,
                                minimum_occupancy>;
                            Run(kernel);
                        }
                    }
                    // Tail number could be One to Seven
                    else if constexpr(BlkGemmPipelineVer == BlockGemmPipelineVersion::v2)
                    {
                        if(gemm_arg.KBatch > 1)
                        {
                            if constexpr(IsSplitKSupported)
                            {
                                if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) ==
                                   TailNumber::One)
                                {
                                    const auto kernel =
                                        kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                            GridwiseGemm,
                                            DeviceOp::AGridDesc_AK0_M_AK1,
                                            DeviceOp::BGridDesc_BK0_N_BK1,
                                            DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            true,
                                            InMemoryDataOperationEnum::AtomicAdd,
                                            minimum_occupancy,
                                            TailNumber::One>;
                                    Run(kernel);
                                }
                                else if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) ==
                                        TailNumber::Full)
                                {
                                    const auto kernel =
                                        kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                            GridwiseGemm,
                                            DeviceOp::AGridDesc_AK0_M_AK1,
                                            DeviceOp::BGridDesc_BK0_N_BK1,
                                            DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            true,
                                            InMemoryDataOperationEnum::AtomicAdd,
                                            minimum_occupancy,
                                            TailNumber::Full>;
                                    Run(kernel);
                                }

                                if constexpr(GridwiseGemm::BlockwiseGemmPipe::PrefetchStages > 2)
                                {
                                    if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) ==
                                       TailNumber::Two)
                                    {
                                        const auto kernel =
                                            kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                                GridwiseGemm,
                                                DeviceOp::AGridDesc_AK0_M_AK1,
                                                DeviceOp::BGridDesc_BK0_N_BK1,
                                                DeviceOp::
                                                    EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                                ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                                ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                                true,
                                                InMemoryDataOperationEnum::AtomicAdd,
                                                minimum_occupancy,
                                                TailNumber::Two>;
                                        Run(kernel);
                                    }
                                }

                                if constexpr(GridwiseGemm::BlockwiseGemmPipe::PrefetchStages > 3)
                                {
                                    if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) ==
                                       TailNumber::Three)
                                    {
                                        const auto kernel =
                                            kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                                GridwiseGemm,
                                                DeviceOp::AGridDesc_AK0_M_AK1,
                                                DeviceOp::BGridDesc_BK0_N_BK1,
                                                DeviceOp::
                                                    EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                                ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                                ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                                true,
                                                InMemoryDataOperationEnum::AtomicAdd,
                                                minimum_occupancy,
                                                TailNumber::Three>;
                                        Run(kernel);
                                    }
                                }

                                if constexpr(GridwiseGemm::BlockwiseGemmPipe::PrefetchStages > 4)
                                {
                                    if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) ==
                                       TailNumber::Four)
                                    {
                                        const auto kernel =
                                            kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                                GridwiseGemm,
                                                DeviceOp::AGridDesc_AK0_M_AK1,
                                                DeviceOp::BGridDesc_BK0_N_BK1,
                                                DeviceOp::
                                                    EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                                ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                                ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                                true,
                                                InMemoryDataOperationEnum::AtomicAdd,
                                                minimum_occupancy,
                                                TailNumber::Four>;
                                        Run(kernel);
                                    }
                                }

                                if constexpr(GridwiseGemm::BlockwiseGemmPipe::PrefetchStages > 5)
                                {
                                    if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) ==
                                       TailNumber::Five)
                                    {
                                        const auto kernel =
                                            kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                                GridwiseGemm,
                                                DeviceOp::AGridDesc_AK0_M_AK1,
                                                DeviceOp::BGridDesc_BK0_N_BK1,
                                                DeviceOp::
                                                    EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                                ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                                ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                                true,
                                                InMemoryDataOperationEnum::AtomicAdd,
                                                minimum_occupancy,
                                                TailNumber::Five>;
                                        Run(kernel);
                                    }
                                }

                                if constexpr(GridwiseGemm::BlockwiseGemmPipe::PrefetchStages > 6)
                                {
                                    if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) ==
                                       TailNumber::Six)
                                    {
                                        const auto kernel =
                                            kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                                GridwiseGemm,
                                                DeviceOp::AGridDesc_AK0_M_AK1,
                                                DeviceOp::BGridDesc_BK0_N_BK1,
                                                DeviceOp::
                                                    EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                                ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                                ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                                true,
                                                InMemoryDataOperationEnum::AtomicAdd,
                                                minimum_occupancy,
                                                TailNumber::Six>;
                                        Run(kernel);
                                    }
                                }

                                if constexpr(GridwiseGemm::BlockwiseGemmPipe::PrefetchStages > 7)
                                {
                                    if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) ==
                                       TailNumber::Seven)
                                    {
                                        const auto kernel =
                                            kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                                GridwiseGemm,
                                                DeviceOp::AGridDesc_AK0_M_AK1,
                                                DeviceOp::BGridDesc_BK0_N_BK1,
                                                DeviceOp::
                                                    EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                                ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                                ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                                true,
                                                InMemoryDataOperationEnum::AtomicAdd,
                                                minimum_occupancy,
                                                TailNumber::Seven>;
                                        Run(kernel);
                                    }
                                }
                            }
                        }
                        else
                        {
                            if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) == TailNumber::One)
                            {
                                const auto kernel = kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                    GridwiseGemm,
                                    DeviceOp::AGridDesc_AK0_M_AK1,
                                    DeviceOp::BGridDesc_BK0_N_BK1,
                                    DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                    ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                    ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                    true,
                                    InMemoryDataOperationEnum::Set,
                                    minimum_occupancy,
                                    TailNumber::One>;
                                Run(kernel);
                            }
                            else if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) ==
                                    TailNumber::Full)
                            {
                                const auto kernel = kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                    GridwiseGemm,
                                    DeviceOp::AGridDesc_AK0_M_AK1,
                                    DeviceOp::BGridDesc_BK0_N_BK1,
                                    DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                    ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                    ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                    true,
                                    InMemoryDataOperationEnum::Set,
                                    minimum_occupancy,
                                    TailNumber::Full>;
                                Run(kernel);
                            }

                            if constexpr(GridwiseGemm::BlockwiseGemmPipe::PrefetchStages > 2)
                            {
                                if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) ==
                                   TailNumber::Two)
                                {
                                    const auto kernel =
                                        kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                            GridwiseGemm,
                                            DeviceOp::AGridDesc_AK0_M_AK1,
                                            DeviceOp::BGridDesc_BK0_N_BK1,
                                            DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            true,
                                            InMemoryDataOperationEnum::Set,
                                            minimum_occupancy,
                                            TailNumber::Two>;
                                    Run(kernel);
                                }
                            }

                            if constexpr(GridwiseGemm::BlockwiseGemmPipe::PrefetchStages > 3)
                            {
                                if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) ==
                                   TailNumber::Three)
                                {
                                    const auto kernel =
                                        kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                            GridwiseGemm,
                                            DeviceOp::AGridDesc_AK0_M_AK1,
                                            DeviceOp::BGridDesc_BK0_N_BK1,
                                            DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            true,
                                            InMemoryDataOperationEnum::Set,
                                            minimum_occupancy,
                                            TailNumber::Three>;
                                    Run(kernel);
                                }
                            }

                            if constexpr(GridwiseGemm::BlockwiseGemmPipe::PrefetchStages > 4)
                            {
                                if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) ==
                                   TailNumber::Four)
                                {
                                    const auto kernel =
                                        kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                            GridwiseGemm,
                                            DeviceOp::AGridDesc_AK0_M_AK1,
                                            DeviceOp::BGridDesc_BK0_N_BK1,
                                            DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            true,
                                            InMemoryDataOperationEnum::Set,
                                            minimum_occupancy,
                                            TailNumber::Four>;
                                    Run(kernel);
                                }
                            }

                            if constexpr(GridwiseGemm::BlockwiseGemmPipe::PrefetchStages > 5)
                            {
                                if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) ==
                                   TailNumber::Five)
                                {
                                    const auto kernel =
                                        kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                            GridwiseGemm,
                                            DeviceOp::AGridDesc_AK0_M_AK1,
                                            DeviceOp::BGridDesc_BK0_N_BK1,
                                            DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            true,
                                            InMemoryDataOperationEnum::Set,
                                            minimum_occupancy,
                                            TailNumber::Five>;
                                    Run(kernel);
                                }
                            }

                            if constexpr(GridwiseGemm::BlockwiseGemmPipe::PrefetchStages > 6)
                            {
                                if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) ==
                                   TailNumber::Six)
                                {
                                    const auto kernel =
                                        kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                            GridwiseGemm,
                                            DeviceOp::AGridDesc_AK0_M_AK1,
                                            DeviceOp::BGridDesc_BK0_N_BK1,
                                            DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            true,
                                            InMemoryDataOperationEnum::Set,
                                            minimum_occupancy,
                                            TailNumber::Six>;
                                    Run(kernel);
                                }
                            }

                            if constexpr(GridwiseGemm::BlockwiseGemmPipe::PrefetchStages > 7)
                            {
                                if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) ==
                                   TailNumber::Seven)
                                {
                                    const auto kernel =
                                        kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                            GridwiseGemm,
                                            DeviceOp::AGridDesc_AK0_M_AK1,
                                            DeviceOp::BGridDesc_BK0_N_BK1,
                                            DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            true,
                                            InMemoryDataOperationEnum::Set,
                                            minimum_occupancy,
                                            TailNumber::Seven>;
                                    Run(kernel);
                                }
                            }
                        }
                    }
                    // Tail number could be Odd or Even
                    else if constexpr(BlkGemmPipelineVer == BlockGemmPipelineVersion::v4)
                    {
                        if(gemm_arg.KBatch > 1)
                        {
                            if constexpr(IsSplitKSupported)
                            {
                                if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) ==
                                   TailNumber::Odd)
                                {
                                    const auto kernel =
                                        kernel_grouped_conv_bwd_data_xdl_cshuffle_v3_2lds<
                                            GridwiseGemm,
                                            DeviceOp::AGridDesc_AK0_M_AK1,
                                            DeviceOp::BGridDesc_BK0_N_BK1,
                                            DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            true,
                                            InMemoryDataOperationEnum::AtomicAdd,
                                            minimum_occupancy,
                                            TailNumber::Odd>;
                                    Run(kernel);
                                }
                                else
                                {
                                    const auto kernel =
                                        kernel_grouped_conv_bwd_data_xdl_cshuffle_v3_2lds<
                                            GridwiseGemm,
                                            DeviceOp::AGridDesc_AK0_M_AK1,
                                            DeviceOp::BGridDesc_BK0_N_BK1,
                                            DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            true,
                                            InMemoryDataOperationEnum::AtomicAdd,
                                            minimum_occupancy,
                                            TailNumber::Even>;
                                    Run(kernel);
                                }
                            }
                        }
                        else
                        {
                            if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) == TailNumber::Odd)
                            {
                                const auto kernel =
                                    kernel_grouped_conv_bwd_data_xdl_cshuffle_v3_2lds<
                                        GridwiseGemm,
                                        DeviceOp::AGridDesc_AK0_M_AK1,
                                        DeviceOp::BGridDesc_BK0_N_BK1,
                                        DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                        ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                        ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                        true,
                                        InMemoryDataOperationEnum::Set,
                                        minimum_occupancy,
                                        TailNumber::Odd>;
                                Run(kernel);
                            }
                            else
                            {
                                const auto kernel =
                                    kernel_grouped_conv_bwd_data_xdl_cshuffle_v3_2lds<
                                        GridwiseGemm,
                                        DeviceOp::AGridDesc_AK0_M_AK1,
                                        DeviceOp::BGridDesc_BK0_N_BK1,
                                        DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                        ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                        ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                        true,
                                        InMemoryDataOperationEnum::Set,
                                        minimum_occupancy,
                                        TailNumber::Even>;
                                Run(kernel);
                            }
                        }
                    }
                    else
                    {
                        if(gemm_arg.KBatch > 1)
                        {
                            if constexpr(IsSplitKSupported)
                            {
                                if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) ==
                                   TailNumber::Odd)
                                {
                                    const auto kernel =
                                        kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                            GridwiseGemm,
                                            DeviceOp::AGridDesc_AK0_M_AK1,
                                            DeviceOp::BGridDesc_BK0_N_BK1,
                                            DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            true,
                                            InMemoryDataOperationEnum::AtomicAdd,
                                            minimum_occupancy,
                                            TailNumber::Odd>;
                                    Run(kernel);
                                }
                                else
                                {
                                    const auto kernel =
                                        kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                            GridwiseGemm,
                                            DeviceOp::AGridDesc_AK0_M_AK1,
                                            DeviceOp::BGridDesc_BK0_N_BK1,
                                            DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                            true,
                                            InMemoryDataOperationEnum::AtomicAdd,
                                            minimum_occupancy,
                                            TailNumber::Even>;
                                    Run(kernel);
                                }
                            }
                        }
                        else
                        {
                            if(GridwiseGemm::CalculateKBlockLoopTailNum(K_split) == TailNumber::Odd)
                            {
                                const auto kernel = kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                    GridwiseGemm,
                                    DeviceOp::AGridDesc_AK0_M_AK1,
                                    DeviceOp::BGridDesc_BK0_N_BK1,
                                    DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                    ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                    ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                    true,
                                    InMemoryDataOperationEnum::Set,
                                    minimum_occupancy,
                                    TailNumber::Odd>;
                                Run(kernel);
                            }
                            else
                            {
                                const auto kernel = kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                    GridwiseGemm,
                                    DeviceOp::AGridDesc_AK0_M_AK1,
                                    DeviceOp::BGridDesc_BK0_N_BK1,
                                    DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                    ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                    ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                    true,
                                    InMemoryDataOperationEnum::Set,
                                    minimum_occupancy,
                                    TailNumber::Even>;
                                Run(kernel);
                            }
                        }
                    }
                }
                else
                {
                    // Tail number always 1
                    if constexpr(BlkGemmPipelineVer == BlockGemmPipelineVersion::v1)
                    {
                        if(gemm_arg.KBatch > 1)
                        {
                            if constexpr(IsSplitKSupported)
                            {
                                const auto kernel = kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                    GridwiseGemm,
                                    DeviceOp::AGridDesc_AK0_M_AK1,
                                    DeviceOp::BGridDesc_BK0_N_BK1,
                                    DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                    ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                    ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                    false,
                                    InMemoryDataOperationEnum::AtomicAdd,
                                    minimum_occupancy>;
                                Run(kernel);
                            }
                        }
                        else
                        {
                            const auto kernel = kernel_grouped_conv_bwd_data_xdl_cshuffle_v3<
                                GridwiseGemm,
                                DeviceOp::AGridDesc_AK0_M_AK1,
                                DeviceOp::BGridDesc_BK0_N_BK1,
                                DeviceOp::EGridDesc_MBlock_MPerBlock_NBlock_NPerBlock,
                                ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                ComputePtrOffsetOfStridedBatch<I1, I1, I0>,
                                false,
                                InMemoryDataOperationEnum::Set,
                                minimum_occupancy>;
                            Run(kernel);
                        }
                    }
                }
            }
            return ave_time;
        }

        float Run(const Argument& arg, const StreamConfig& stream_config = StreamConfig{})
        {
            float ave_time = 0;

            if(stream_config.log_level_ > 0)
            {
                arg.Print();
            }
            // Transpose from NGKHW to NHWGK
            if constexpr(is_NGCHW_NGKHW<ELayout, BLayout, ALayout>() ||
                         is_NGCDHW_NGKDHW<ELayout, BLayout, ALayout>())
            {
                EDataType* p_e_in_grid =
                    type_convert<EDataType*>(arg.p_workspace_) +
                    (arg.GetWorkspaceATensorSizeBytes() + arg.GetWorkspaceBTensorSizeBytes()) /
                        sizeof(EDataType);

                const auto clear_workspace = [&]() {
                    hip_check_error(hipMemsetAsync(p_e_in_grid,
                                                   0,
                                                   arg.GetWorkspaceETensorSizeBytes(),
                                                   stream_config.stream_id_));
                };

                const index_t a_grid_size =
                    arg.elementwise_block_2_ctile_map_transpose_a_.CalculateGridSize(
                        arg.a_in_transpose_desc_) *
                    arg.num_workgroups_per_Conv_N_;
                const index_t b_grid_size =
                    (is_NGCHW_GKCYX_NGKHW<ELayout, BLayout, ALayout>() ||
                     is_NGCDHW_GKCZYX_NGKDHW<ELayout, BLayout, ALayout>())
                        ? arg.elementwise_block_2_ctile_map_transpose_b_.CalculateGridSize(
                              arg.b_in_transpose_desc_)
                        : 0; // Dont run transpose B if not needed

                ADataType* p_a_out_grid = type_convert<ADataType*>(arg.p_workspace_);
                BDataType* p_b_out_grid = type_convert<BDataType*>(arg.p_workspace_) +
                                          arg.GetWorkspaceATensorSizeBytes() / sizeof(BDataType);

                auto kernel_transpose =
                    kernel_elementwise_batched_dual<GridwiseElementwiseInputTranspose,
                                                    GridwiseElementwiseWeightTranspose,
                                                    ck::Tuple<NGCHWTransposeDescType>,
                                                    ck::Tuple<GKCYXTransposeDescType>,
                                                    ck::Tuple<NHWGCTransposeDescType>,
                                                    ck::Tuple<GKYXCTransposeDescType>,
                                                    ck::Tuple<const ADataType*>,
                                                    ck::Tuple<const BDataType*>,
                                                    ck::Tuple<ADataType*>,
                                                    ck::Tuple<BDataType*>,
                                                    Block2TileMapInOutElementwise,
                                                    Block2TileMapWeiElementwise,
                                                    element_wise::PassThrough,
                                                    I1,
                                                    I1,
                                                    I1,
                                                    I1>;

                ave_time += launch_and_time_kernel_with_preprocess(
                    stream_config,
                    clear_workspace,
                    kernel_transpose,
                    dim3(a_grid_size + b_grid_size),
                    dim3(ElementwiseBlocksize),
                    0,
                    make_tuple(arg.a_in_transpose_desc_),
                    make_tuple(arg.b_in_transpose_desc_),
                    make_tuple(arg.a_out_transpose_desc_),
                    make_tuple(arg.b_out_transpose_desc_),
                    make_tuple(arg.p_a_grid_),
                    make_tuple(arg.p_b_grid_),
                    make_tuple(p_a_out_grid),
                    make_tuple(p_b_out_grid),
                    arg.elementwise_block_2_ctile_map_transpose_a_,
                    arg.elementwise_block_2_ctile_map_transpose_b_,
                    element_wise::PassThrough{},
                    a_grid_size,
                    arg.num_workgroups_per_Conv_N_,
                    I1, // B is not splited per N
                    std::array<index_t, I1>{
                        static_cast<index_t>(arg.compute_ptr_offset_of_workspace_n_.BatchStrideA_)},
                    std::array<index_t, I1>{0},
                    std::array<index_t, I1>{
                        static_cast<index_t>(arg.compute_ptr_offset_of_n_.BatchStrideA_)},
                    std::array<index_t, I1>{0});
            }

            if constexpr(isMultiD)
            {
                ave_time += RunMultiDGemm(arg, stream_config);
            }
            else
            {
                ave_time += RunGemmV3(arg, stream_config);
            }

            // Transpose from NHWGC to NGCHW
            if constexpr(is_NGCHW_NGKHW<ELayout, BLayout, ALayout>() ||
                         is_NGCDHW_NGKDHW<ELayout, BLayout, ALayout>())
            {
                const index_t grid_size =
                    arg.elementwise_block_2_ctile_map_transpose_e_.CalculateGridSize(
                        arg.e_in_transpose_desc_) *
                    arg.num_workgroups_per_Conv_N_;

                const EDataType* p_e_in_grid =
                    type_convert<EDataType*>(arg.p_workspace_) +
                    (arg.GetWorkspaceATensorSizeBytes() + arg.GetWorkspaceBTensorSizeBytes()) /
                        sizeof(EDataType);

                EDataType* p_e_out_grid = arg.p_e_grid_;

                auto kernel_transpose =
                    kernel_batched_elementwise<GridwiseElementwiseOutputTranspose,
                                               ck::Tuple<NHWGCTransposeDescType>,
                                               ck::Tuple<NGCHWTransposeDescType>,
                                               ck::Tuple<const EDataType*>,
                                               ck::Tuple<EDataType*>,
                                               Block2TileMapInOutElementwise,
                                               element_wise::PassThrough,
                                               I1,
                                               I1>;

                ave_time += launch_and_time_kernel(
                    stream_config,
                    kernel_transpose,
                    dim3(grid_size),
                    dim3(ElementwiseBlocksize),
                    0,
                    make_tuple(arg.e_in_transpose_desc_),
                    make_tuple(arg.e_out_transpose_desc_),
                    make_tuple(p_e_in_grid),
                    make_tuple(p_e_out_grid),
                    arg.elementwise_block_2_ctile_map_transpose_e_,
                    element_wise::PassThrough{},
                    arg.num_workgroups_per_Conv_N_,
                    std::array<index_t, I1>{
                        static_cast<index_t>(arg.compute_ptr_offset_of_n_.BatchStrideE_)},
                    std::array<index_t, I1>{static_cast<index_t>(
                        arg.compute_ptr_offset_of_workspace_n_.BatchStrideE_)});
            }

            return ave_time;
        }

        float Run(const BaseArgument* p_arg,
                  const StreamConfig& stream_config = StreamConfig{}) override
        {
            return Run(*dynamic_cast<const Argument*>(p_arg), stream_config);
        }
    };

    static bool IsSupportedArgument(const Argument& arg)
    {
        if(!ck::is_xdl_supported())
        {
            return false;
        }

        if(!is_bf16_atomic_supported() && std::is_same_v<EDataType, ck::bhalf_t> &&
           arg.k_batch_ > 1)
        {
            return false;
        }

        if constexpr(!IsSplitKSupported)
        {
            if(arg.k_batch_ != 1)
            {
                return false;
            }
        }

        const index_t ConvG = arg.b_g_k_c_xs_lengths_[0];
        const index_t ConvK = arg.b_g_k_c_xs_lengths_[1];
        const index_t ConvC = arg.b_g_k_c_xs_lengths_[2];

        if constexpr(!isMultiD)
        {
            for(std::size_t i = 0; i < arg.a_grid_desc_ak0_m_ak1_container_.size(); i++)
            {
                const index_t GemmM = arg.a_grid_desc_ak0_m_ak1_container_[i].GetLength(I1);
                const index_t GemmN = arg.b_grid_desc_bk0_n_bk1_container_[i].GetLength(I1);
                const index_t GemmK = arg.a_grid_desc_ak0_m_ak1_container_[i].GetLength(I0) *
                                      arg.a_grid_desc_ak0_m_ak1_container_[i].GetLength(I2);

                typename GridwiseGemm::Argument gemm_arg{
                    nullptr, nullptr, nullptr, GemmM, GemmN, GemmK, I0, I0, I0, arg.k_batch_};

                const auto num_k_loop = gemm_arg.AK0 / (KPerBlock / AK1);
                if constexpr(BlkGemmPipelineVer != BlockGemmPipelineVersion::v1)
                {
                    if(num_k_loop <= GridwiseGemm::BlockwiseGemmPipe::PrefetchStages)
                    {
                        return false;
                    }
                }
            }
        }

        // Specifialization
        if constexpr(ConvBackwardDataSpecialization ==
                     ConvolutionBackwardDataSpecialization::Filter1x1Stride1Pad0)
        {
            // check if it's 1x1, stride=1 pad = 0 conv
            for(int i = 0; i < NDimSpatial; i++)
            {
                if(!(arg.b_g_k_c_xs_lengths_[3 + i] == 1 && arg.conv_filter_strides_[i] == 1 &&
                     arg.input_left_pads_[i] == 0 && arg.input_right_pads_[i] == 0))
                {
                    return false;
                }
            }
        }

        // vector load for A matrix from global memory to LDS
        if constexpr(is_same_v<ALayout, tensor_layout::convolution::GNHWK> ||
                     is_same_v<ALayout, tensor_layout::convolution::GNDHWK> ||
                     is_same_v<ALayout, tensor_layout::convolution::NHWGK> ||
                     is_same_v<ALayout, tensor_layout::convolution::NDHWGK> ||
                     is_same_v<ALayout, tensor_layout::convolution::NGKHW> ||
                     is_same_v<ALayout, tensor_layout::convolution::NGKDHW>)
        {
            if(!(ABlockTransferSrcVectorDim == 2 && ConvK % ABlockTransferSrcScalarPerVector == 0))
            {
                return false;
            }
        }
        else
        {
            return false;
        }

        // vector load for B matrix from global memory to LDS
        if constexpr(is_same_v<BLayout, tensor_layout::convolution::GKYXC> ||
                     is_same_v<BLayout, tensor_layout::convolution::GKZYXC> ||
                     is_same_v<BLayout, tensor_layout::convolution::GKCYX> ||
                     is_same_v<BLayout, tensor_layout::convolution::GKCZYX>)
        {
            if(!(BBlockTransferSrcVectorDim == 1 && ConvC % BBlockTransferSrcScalarPerVector == 0))
            {
                return false;
            }
        }
        else
        {
            return false;
        }

        // vector store for Ds
        bool ds_valid = true;

        static_for<0, NumDTensor, 1>{}([&](auto i) {
            using DLayout = remove_cvref_t<tuple_element_t<i.value, DsLayout>>;

            if constexpr(is_same_v<DLayout, tensor_layout::convolution::GNHWC> ||
                         is_same_v<DLayout, tensor_layout::convolution::GNDHWC> ||
                         is_same_v<DLayout, tensor_layout::convolution::NHWGC> ||
                         is_same_v<DLayout, tensor_layout::convolution::NDHWGC> ||
                         is_same_v<DLayout, tensor_layout::convolution::G_NHW_C> ||
                         is_same_v<DLayout, tensor_layout::convolution::GC> ||
                         is_same_v<DLayout, tensor_layout::convolution::G_C>)
            {
                // vector load D matrix from global memory
                if(!(ConvC % CDEBlockTransferScalarPerVector_NPerBlock == 0))
                {
                    ds_valid = false;
                }
            }
            else
            {
                ds_valid = false;
            }
        });

        if(!ds_valid)
        {
            return false;
        }

        // vector store for E
        if constexpr(is_same_v<ELayout, tensor_layout::convolution::GNHWC> ||
                     is_same_v<ELayout, tensor_layout::convolution::GNDHWC> ||
                     is_same_v<ELayout, tensor_layout::convolution::NHWGC> ||
                     is_same_v<ELayout, tensor_layout::convolution::NDHWGC> ||
                     is_same_v<ELayout, tensor_layout::convolution::NGCHW> ||
                     is_same_v<ELayout, tensor_layout::convolution::NGCDHW>)
        {
            // vector store C matrix into global memory
            if(!(ConvC % CDEBlockTransferScalarPerVector_NPerBlock == 0))
            {
                return false;
            }
        }
        else
        {
            return false;
        }

        // Gridwise GEMM size
        for(std::size_t i = 0; i < arg.a_grid_desc_ak0_m_ak1_container_.size(); i++)
        {
            if constexpr(isMultiD)
            {
                if(!GridwiseGemm::CheckValidity(arg.a_grid_desc_m_k_container_[i],
                                                arg.b_grid_desc_n_k_container_[i],
                                                arg.ds_grid_desc_m_n_container_[i],
                                                arg.e_grid_desc_m_n_container_[i],
                                                arg.block_2_etile_map_container_[i]))
                {
                    return false;
                }
            }
        }

        if constexpr(is_NGCHW_NGKHW<ELayout, BLayout, ALayout>() ||
                     is_NGCDHW_NGKDHW<ELayout, BLayout, ALayout>())
        {
            if((ConvG * ConvC) % CDEBlockTransferScalarPerVector_NPerBlock != 0)
            {
                return false;
            }

            if((ConvG * ConvK) % CDEBlockTransferScalarPerVector_NPerBlock != 0)
            {
                return false;
            }

            const index_t a_spatial_acum = ck::accumulate_n<index_t>(
                arg.a_g_n_k_wos_lengths_.begin() + I3, NDimSpatial, 1, std::multiplies<>());
            const index_t e_spatial_acum = ck::accumulate_n<index_t>(
                arg.e_g_n_c_wis_lengths_.begin() + I3, NDimSpatial, 1, std::multiplies<>());

            if(a_spatial_acum % TransposeTransferInScalarPerVectorAligned != 0)
            {
                return false;
            }

            if(e_spatial_acum % TransposeTransferOutScalarPerVectorAligned != 0)
            {
                return false;
            }

            if(!arg.p_workspace_)
            {
                if(ck::EnvIsEnabled(CK_ENV(CK_LOGGING)))
                {
                    std::cout
                        << "Warning: Workspace for "
                           "DeviceGroupedConvBwdDataMultipleD_Xdl_CShuffle_v1::Argument is not "
                           "allocated, use SetWorkSpacePointer."
                        << std::endl;
                }
                return false;
            }
        }

        return true;
    }

    bool IsSupportedArgument(const BaseArgument* p_arg) override
    {
        return IsSupportedArgument(*dynamic_cast<const Argument*>(p_arg));
    }

    static auto
    MakeArgument(const void* p_a,                                                 // output image
                 const void* p_b,                                                 // weight
                 const std::array<const void*, NumDTensor>& p_ds,                 // bias
                 void* p_e,                                                       // input image
                 const std::array<index_t, NDimSpatial + 3>& a_g_n_k_wos_lengths, // output image
                 const std::array<index_t, NDimSpatial + 3>& a_g_n_k_wos_strides, // output image
                 const std::array<index_t, NDimSpatial + 3>& b_g_k_c_xs_lengths,  // weight
                 const std::array<index_t, NDimSpatial + 3>& b_g_k_c_xs_strides,  // weight
                 const std::array<std::array<index_t, NDimSpatial + 3>, NumDTensor>&
                     ds_g_n_c_wis_lengths, // bias
                 const std::array<std::array<index_t, NDimSpatial + 3>, NumDTensor>&
                     ds_g_n_c_wis_strides,                                        // bias
                 const std::array<index_t, NDimSpatial + 3>& e_g_n_c_wis_lengths, // input image
                 const std::array<index_t, NDimSpatial + 3>& e_g_n_c_wis_strides, // input image
                 const std::array<index_t, NDimSpatial>& conv_filter_strides,
                 const std::array<index_t, NDimSpatial>& conv_filter_dilations,
                 const std::array<index_t, NDimSpatial>& input_left_pads,
                 const std::array<index_t, NDimSpatial>& input_right_pads,
                 const AElementwiseOp& a_element_op,
                 const BElementwiseOp& b_element_op,
                 const CDEElementwiseOp& cde_element_op,
                 const ck::index_t split_k = 1)
    {
        return Argument{p_a,
                        p_b,
                        p_ds,
                        p_e,
                        a_g_n_k_wos_lengths,
                        a_g_n_k_wos_strides,
                        b_g_k_c_xs_lengths,
                        b_g_k_c_xs_strides,
                        ds_g_n_c_wis_lengths,
                        ds_g_n_c_wis_strides,
                        e_g_n_c_wis_lengths,
                        e_g_n_c_wis_strides,
                        conv_filter_strides,
                        conv_filter_dilations,
                        input_left_pads,
                        input_right_pads,
                        a_element_op,
                        b_element_op,
                        cde_element_op,
                        split_k};
    }

    static auto MakeInvoker() { return Invoker{}; }

    std::unique_ptr<BaseArgument> MakeArgumentPointer(
        const void* p_a,                                                 // output image
        const void* p_b,                                                 // weight
        const std::array<const void*, NumDTensor>& p_ds,                 // bias
        void* p_e,                                                       // input image
        const std::array<index_t, NDimSpatial + 3>& a_g_n_k_wos_lengths, // output image
        const std::array<index_t, NDimSpatial + 3>& a_g_n_k_wos_strides, // output image
        const std::array<index_t, NDimSpatial + 3>& b_g_k_c_xs_lengths,  // weight
        const std::array<index_t, NDimSpatial + 3>& b_g_k_c_xs_strides,  // weight
        const std::array<std::array<index_t, NDimSpatial + 3>, NumDTensor>&
            ds_g_n_c_wis_lengths, // bias
        const std::array<std::array<index_t, NDimSpatial + 3>, NumDTensor>&
            ds_g_n_c_wis_strides,                                        // bias
        const std::array<index_t, NDimSpatial + 3>& e_g_n_c_wis_lengths, // input image
        const std::array<index_t, NDimSpatial + 3>& e_g_n_c_wis_strides, // input image
        const std::array<index_t, NDimSpatial>& conv_filter_strides,
        const std::array<index_t, NDimSpatial>& conv_filter_dilations,
        const std::array<index_t, NDimSpatial>& input_left_pads,
        const std::array<index_t, NDimSpatial>& input_right_pads,
        const AElementwiseOp& a_element_op,
        const BElementwiseOp& b_element_op,
        const CDEElementwiseOp& cde_element_op,
        const ck::index_t split_k = 1) override
    {
        return std::make_unique<Argument>(p_a,
                                          p_b,
                                          p_ds,
                                          p_e,
                                          a_g_n_k_wos_lengths,
                                          a_g_n_k_wos_strides,
                                          b_g_k_c_xs_lengths,
                                          b_g_k_c_xs_strides,
                                          ds_g_n_c_wis_lengths,
                                          ds_g_n_c_wis_strides,
                                          e_g_n_c_wis_lengths,
                                          e_g_n_c_wis_strides,
                                          conv_filter_strides,
                                          conv_filter_dilations,
                                          input_left_pads,
                                          input_right_pads,
                                          a_element_op,
                                          b_element_op,
                                          cde_element_op,
                                          split_k);
    }

    std::unique_ptr<BaseInvoker> MakeInvokerPointer() override
    {
        return std::make_unique<Invoker>(Invoker{});
    }

    std::string GetTypeString() const override
    {
        auto str = std::stringstream();

        std::map<BlockGemmPipelineScheduler, std::string> BlkGemmPipelineSchedulerToString{
            {BlockGemmPipelineScheduler::Intrawave, "Intrawave"},
            {BlockGemmPipelineScheduler::Interwave, "Interwave"}};

        std::map<BlockGemmPipelineVersion, std::string> BlkGemmPipelineVersionToString{
            {BlockGemmPipelineVersion::v1, "v1"},
            {BlockGemmPipelineVersion::v2, "v2"},
            {BlockGemmPipelineVersion::v3, "v3"},
            {BlockGemmPipelineVersion::v4, "v4"},
            {BlockGemmPipelineVersion::v5, "v5"}};

        // clang-format off
        str << "DeviceGroupedConvBwdDataMultipleD_Xdl_CShuffle_v1"
            << "<"
            << BlockSize << ", "
            << MPerBlock << ", "
            << NPerBlock << ", "
            << KPerBlock << ", "
            << AK1 << ", "
            << BK1 << ", "
            << getConvBackwardDataSpecializationString(ConvBackwardDataSpecialization) << ", "
            << MPerXDL << ", "
            << NPerXDL << ", "
            << MXdlPerWave << ", "
            << NXdlPerWave << ", "
            << ABlockTransferSrcScalarPerVector << ", "
            << BBlockTransferSrcScalarPerVector << ", "
            << CShuffleMXdlPerWavePerShuffle << ", "
            << CShuffleNXdlPerWavePerShuffle << ", "
            << "BlkGemmPipelineScheduler: "
            << BlkGemmPipelineSchedulerToString[BlkGemmPipeSched] << ", "
            << "BlkGemmPipelineVersion: "
            << BlkGemmPipelineVersionToString[BlkGemmPipelineVer];

            if constexpr(is_NGCHW_NGKHW<ELayout, BLayout, ALayout>() ||
                        is_NGCDHW_NGKDHW<ELayout, BLayout, ALayout>()) {
                    str << ", TransposeTransferInScalarPerVectorAligned: "
                    << TransposeTransferInScalarPerVectorAligned <<", "
                    << "TransposeTransferOutScalarPerVectorAligned: " << TransposeTransferOutScalarPerVectorAligned;
                }
    
                
            str << ">";

        return str.str();
    }

    size_t GetWorkSpaceSize(const BaseArgument* p_arg) const override
    {
        auto arg = dynamic_cast<const Argument*>(p_arg);
        if(arg)
        {
            return arg->GetWorkspaceSizeBytes();
        }
        else
            throw std::runtime_error(
                "The argument pointer is not an object of "
                "DeviceGroupedConvBwdDataMultipleD_Xdl_CShuffle_v1::Argument structure!");
    }

    void SetWorkSpacePointer(BaseArgument* p_arg,
                             void* p_workspace,
                             const StreamConfig& = StreamConfig{}) const override
    {
        auto p_arg_ = dynamic_cast<Argument*>(p_arg);
        if(p_arg_)
        {
            p_arg_->p_workspace_ = p_workspace;
        }
        else
            throw std::runtime_error(
                "The argument pointer is not an object of "
                "DeviceGroupedConvBwdDataMultipleD_Xdl_CShuffle_v1::Argument structure!");
    }
};

} // namespace device
} // namespace tensor_operation
} // namespace ck
