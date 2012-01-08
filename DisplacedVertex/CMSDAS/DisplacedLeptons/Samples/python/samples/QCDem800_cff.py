sampleDataSet = '/QCD_Pt-800to1000_TuneZ2_7TeV_pythia6/Summer11-PU_S3_START42_V11-v2/AODSIM'
sampleCMSEnergy = 7000

sampleRelease = "CMSSW_4_2_2_patch2" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_4_2_7" # release used to create new files with

sampleNumEvents = 4053888

sampleXSec = 1.84 # cross-section times filter efficiency (pb)

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START42_V13::All'
sampleHLTProcess = '*'

sampleBaseDir = "root://xrootd.rcac.purdue.edu//store/user/demattia/longlived/"+sampleProcessRelease+"/QCDem800"

sampleRecoFiles = [ ]

samplePatFiles = [
  sampleBaseDir+"/pat/PATtuple_1_1_W24.root",
  sampleBaseDir+"/pat/PATtuple_2_1_yfp.root",
  sampleBaseDir+"/pat/PATtuple_3_1_Lze.root",
  sampleBaseDir+"/pat/PATtuple_4_1_jwv.root",
  sampleBaseDir+"/pat/PATtuple_5_1_Xpr.root",
  sampleBaseDir+"/pat/PATtuple_6_1_3Xh.root",
  sampleBaseDir+"/pat/PATtuple_7_1_0ZO.root",
  sampleBaseDir+"/pat/PATtuple_8_1_5yy.root",
  sampleBaseDir+"/pat/PATtuple_9_1_nMD.root",
  sampleBaseDir+"/pat/PATtuple_10_1_qnZ.root",
  sampleBaseDir+"/pat/PATtuple_11_1_7NK.root",
  sampleBaseDir+"/pat/PATtuple_12_1_GXw.root",
  sampleBaseDir+"/pat/PATtuple_13_1_1EL.root",
  sampleBaseDir+"/pat/PATtuple_14_1_IhC.root",
  sampleBaseDir+"/pat/PATtuple_15_1_Wyv.root",
  sampleBaseDir+"/pat/PATtuple_16_1_yUn.root",
  sampleBaseDir+"/pat/PATtuple_17_1_zmi.root",
  sampleBaseDir+"/pat/PATtuple_18_1_BYT.root",
  sampleBaseDir+"/pat/PATtuple_19_1_93q.root",
  sampleBaseDir+"/pat/PATtuple_20_1_W5c.root",
  sampleBaseDir+"/pat/PATtuple_21_1_t9J.root",
  sampleBaseDir+"/pat/PATtuple_22_1_awc.root",
  sampleBaseDir+"/pat/PATtuple_23_1_aJk.root",
  sampleBaseDir+"/pat/PATtuple_24_1_rCi.root",
  sampleBaseDir+"/pat/PATtuple_25_1_nPh.root",
  sampleBaseDir+"/pat/PATtuple_26_1_1er.root",
  sampleBaseDir+"/pat/PATtuple_27_1_ALX.root",
  sampleBaseDir+"/pat/PATtuple_28_1_qPj.root",
  sampleBaseDir+"/pat/PATtuple_29_1_FOC.root",
  sampleBaseDir+"/pat/PATtuple_30_1_rOQ.root",
  sampleBaseDir+"/pat/PATtuple_31_1_7ki.root",
  sampleBaseDir+"/pat/PATtuple_32_1_6Wv.root",
  sampleBaseDir+"/pat/PATtuple_33_1_tkz.root",
  sampleBaseDir+"/pat/PATtuple_34_1_hHX.root",
  sampleBaseDir+"/pat/PATtuple_35_1_vPg.root",
  sampleBaseDir+"/pat/PATtuple_36_1_npi.root",
  sampleBaseDir+"/pat/PATtuple_37_1_Mzg.root",
  sampleBaseDir+"/pat/PATtuple_38_1_7bU.root",
  sampleBaseDir+"/pat/PATtuple_39_1_5EB.root",
  sampleBaseDir+"/pat/PATtuple_40_1_kLZ.root",
  sampleBaseDir+"/pat/PATtuple_41_1_3tw.root",
  sampleBaseDir+"/pat/PATtuple_42_1_XJ9.root",
  sampleBaseDir+"/pat/PATtuple_43_1_GTE.root",
  sampleBaseDir+"/pat/PATtuple_44_1_2eg.root",
  sampleBaseDir+"/pat/PATtuple_45_1_eVJ.root",
  sampleBaseDir+"/pat/PATtuple_46_1_7if.root",
  sampleBaseDir+"/pat/PATtuple_47_1_70Z.root",
  sampleBaseDir+"/pat/PATtuple_48_1_vlS.root",
  sampleBaseDir+"/pat/PATtuple_49_1_jfE.root",
  sampleBaseDir+"/pat/PATtuple_50_1_4XR.root",
  sampleBaseDir+"/pat/PATtuple_51_1_CEl.root",
  sampleBaseDir+"/pat/PATtuple_52_1_nU7.root",
  sampleBaseDir+"/pat/PATtuple_53_1_fdV.root",
  sampleBaseDir+"/pat/PATtuple_54_1_G8Z.root",
  sampleBaseDir+"/pat/PATtuple_55_1_XEx.root",
  sampleBaseDir+"/pat/PATtuple_56_1_XOx.root",
  sampleBaseDir+"/pat/PATtuple_57_1_08s.root",
  sampleBaseDir+"/pat/PATtuple_58_1_qSM.root",
  sampleBaseDir+"/pat/PATtuple_59_1_Yc5.root",
  sampleBaseDir+"/pat/PATtuple_60_1_uvI.root",
  sampleBaseDir+"/pat/PATtuple_61_1_TRb.root",
  sampleBaseDir+"/pat/PATtuple_62_1_47q.root",
  sampleBaseDir+"/pat/PATtuple_63_1_xj6.root",
  sampleBaseDir+"/pat/PATtuple_64_1_Opz.root",
  sampleBaseDir+"/pat/PATtuple_65_1_tNL.root",
  sampleBaseDir+"/pat/PATtuple_66_1_D23.root",
  sampleBaseDir+"/pat/PATtuple_67_1_evC.root",
  sampleBaseDir+"/pat/PATtuple_68_1_oXj.root",
  sampleBaseDir+"/pat/PATtuple_69_1_SOj.root",
  sampleBaseDir+"/pat/PATtuple_70_1_4hU.root",
  sampleBaseDir+"/pat/PATtuple_71_1_wkg.root",
  sampleBaseDir+"/pat/PATtuple_72_1_z6A.root",
  sampleBaseDir+"/pat/PATtuple_73_1_1ye.root",
  sampleBaseDir+"/pat/PATtuple_74_1_7dj.root",
  sampleBaseDir+"/pat/PATtuple_75_1_4Fs.root",
  sampleBaseDir+"/pat/PATtuple_76_1_tzh.root",
  sampleBaseDir+"/pat/PATtuple_77_1_SaQ.root",
  sampleBaseDir+"/pat/PATtuple_78_1_S9W.root",
  sampleBaseDir+"/pat/PATtuple_79_1_kQ7.root",
  sampleBaseDir+"/pat/PATtuple_80_1_qBj.root",
  sampleBaseDir+"/pat/PATtuple_81_1_F7J.root",
  sampleBaseDir+"/pat/PATtuple_82_1_Pgn.root",
  sampleBaseDir+"/pat/PATtuple_83_1_x0t.root",
  sampleBaseDir+"/pat/PATtuple_84_1_ru5.root",
  sampleBaseDir+"/pat/PATtuple_85_1_ffR.root",
  sampleBaseDir+"/pat/PATtuple_86_1_Zw4.root",
  sampleBaseDir+"/pat/PATtuple_87_1_idu.root",
  sampleBaseDir+"/pat/PATtuple_88_1_GBf.root",
  sampleBaseDir+"/pat/PATtuple_89_1_GeG.root",
  sampleBaseDir+"/pat/PATtuple_90_1_PcM.root",
  sampleBaseDir+"/pat/PATtuple_91_1_MBk.root",
  sampleBaseDir+"/pat/PATtuple_92_1_QlM.root",
  sampleBaseDir+"/pat/PATtuple_93_1_Jqd.root",
  sampleBaseDir+"/pat/PATtuple_94_1_y65.root",
  sampleBaseDir+"/pat/PATtuple_95_1_TaB.root",
  sampleBaseDir+"/pat/PATtuple_96_1_Q6o.root",
  sampleBaseDir+"/pat/PATtuple_97_1_k7w.root",
  sampleBaseDir+"/pat/PATtuple_98_1_IGq.root",
  sampleBaseDir+"/pat/PATtuple_99_1_jou.root",
  sampleBaseDir+"/pat/PATtuple_100_1_EcU.root",
  sampleBaseDir+"/pat/PATtuple_101_1_tpO.root",
  sampleBaseDir+"/pat/PATtuple_102_1_Al2.root",
  sampleBaseDir+"/pat/PATtuple_103_1_Oco.root",
  sampleBaseDir+"/pat/PATtuple_104_1_Viu.root",
  sampleBaseDir+"/pat/PATtuple_105_1_1vU.root",
  sampleBaseDir+"/pat/PATtuple_106_1_As4.root",
  sampleBaseDir+"/pat/PATtuple_107_1_ged.root",
  sampleBaseDir+"/pat/PATtuple_108_1_fDJ.root",
  sampleBaseDir+"/pat/PATtuple_109_1_Mwn.root",
  sampleBaseDir+"/pat/PATtuple_110_1_VR7.root",
  sampleBaseDir+"/pat/PATtuple_111_1_7Yc.root",
  sampleBaseDir+"/pat/PATtuple_112_1_1Z4.root",
  sampleBaseDir+"/pat/PATtuple_113_1_n6o.root",
  sampleBaseDir+"/pat/PATtuple_114_1_g7v.root",
  sampleBaseDir+"/pat/PATtuple_115_1_JtR.root",
  sampleBaseDir+"/pat/PATtuple_116_1_PgV.root",
  sampleBaseDir+"/pat/PATtuple_117_1_Gva.root",
  sampleBaseDir+"/pat/PATtuple_118_1_tcj.root",
  sampleBaseDir+"/pat/PATtuple_119_1_r1R.root",
  sampleBaseDir+"/pat/PATtuple_120_1_Zl5.root",
  sampleBaseDir+"/pat/PATtuple_121_1_Zyd.root",
  sampleBaseDir+"/pat/PATtuple_122_1_FQu.root",
  sampleBaseDir+"/pat/PATtuple_123_1_p1v.root",
  sampleBaseDir+"/pat/PATtuple_124_1_Xzc.root",
  sampleBaseDir+"/pat/PATtuple_125_1_0Lx.root",
  sampleBaseDir+"/pat/PATtuple_126_1_WLz.root",
  sampleBaseDir+"/pat/PATtuple_127_1_HCS.root",
  sampleBaseDir+"/pat/PATtuple_128_1_01t.root",
  sampleBaseDir+"/pat/PATtuple_129_1_c9s.root",
  sampleBaseDir+"/pat/PATtuple_130_1_EAo.root",
  sampleBaseDir+"/pat/PATtuple_131_1_sCF.root",
  sampleBaseDir+"/pat/PATtuple_132_1_u4a.root",
  sampleBaseDir+"/pat/PATtuple_133_1_zye.root",
  sampleBaseDir+"/pat/PATtuple_134_1_fuj.root",
  sampleBaseDir+"/pat/PATtuple_135_1_If4.root",
  sampleBaseDir+"/pat/PATtuple_136_1_vIi.root",
  sampleBaseDir+"/pat/PATtuple_137_1_9Sc.root",
  sampleBaseDir+"/pat/PATtuple_138_1_Cdp.root",
  sampleBaseDir+"/pat/PATtuple_139_1_CEk.root",
  sampleBaseDir+"/pat/PATtuple_140_1_S1P.root",
  sampleBaseDir+"/pat/PATtuple_141_1_4LX.root",
  sampleBaseDir+"/pat/PATtuple_142_1_iLV.root",
  sampleBaseDir+"/pat/PATtuple_143_1_qSC.root",
  sampleBaseDir+"/pat/PATtuple_144_1_qZd.root",
  sampleBaseDir+"/pat/PATtuple_145_1_rLQ.root",
  sampleBaseDir+"/pat/PATtuple_146_1_Fhz.root",
  sampleBaseDir+"/pat/PATtuple_147_1_3pX.root",
  sampleBaseDir+"/pat/PATtuple_148_1_PHK.root",
  sampleBaseDir+"/pat/PATtuple_149_1_eha.root",
  sampleBaseDir+"/pat/PATtuple_150_1_NV5.root",
  sampleBaseDir+"/pat/PATtuple_151_1_t6L.root",
  sampleBaseDir+"/pat/PATtuple_152_1_wUR.root",
  sampleBaseDir+"/pat/PATtuple_153_1_0lj.root",
  sampleBaseDir+"/pat/PATtuple_154_1_Gzb.root",
  sampleBaseDir+"/pat/PATtuple_155_1_V47.root",
  sampleBaseDir+"/pat/PATtuple_156_1_kK6.root",
  sampleBaseDir+"/pat/PATtuple_157_1_CLO.root",
  sampleBaseDir+"/pat/PATtuple_158_1_rMe.root",
  sampleBaseDir+"/pat/PATtuple_159_1_uxm.root",
  sampleBaseDir+"/pat/PATtuple_160_1_Eki.root",
  sampleBaseDir+"/pat/PATtuple_161_1_8x3.root",
  sampleBaseDir+"/pat/PATtuple_162_1_IiS.root",
  sampleBaseDir+"/pat/PATtuple_163_1_9gp.root",
  sampleBaseDir+"/pat/PATtuple_164_1_Ye3.root",
  sampleBaseDir+"/pat/PATtuple_165_1_igL.root",
  sampleBaseDir+"/pat/PATtuple_166_1_C0l.root",
  sampleBaseDir+"/pat/PATtuple_167_1_Npk.root",
  sampleBaseDir+"/pat/PATtuple_168_1_NaL.root",
  sampleBaseDir+"/pat/PATtuple_169_1_8Mk.root",
  sampleBaseDir+"/pat/PATtuple_170_1_7Ia.root",
  sampleBaseDir+"/pat/PATtuple_171_1_yJo.root",
  sampleBaseDir+"/pat/PATtuple_172_1_Xt2.root",
  sampleBaseDir+"/pat/PATtuple_173_1_yUG.root",
  sampleBaseDir+"/pat/PATtuple_174_1_Oki.root",
  sampleBaseDir+"/pat/PATtuple_175_1_Oza.root",
  sampleBaseDir+"/pat/PATtuple_176_1_tmM.root",
  sampleBaseDir+"/pat/PATtuple_177_1_Ts9.root",
  sampleBaseDir+"/pat/PATtuple_178_1_sz5.root",
  sampleBaseDir+"/pat/PATtuple_180_1_j4t.root",
  sampleBaseDir+"/pat/PATtuple_181_1_uY5.root",
  sampleBaseDir+"/pat/PATtuple_182_1_Aij.root",
  sampleBaseDir+"/pat/PATtuple_183_1_CEt.root",
  sampleBaseDir+"/pat/PATtuple_184_1_nsF.root",
  sampleBaseDir+"/pat/PATtuple_185_1_AUd.root",
  sampleBaseDir+"/pat/PATtuple_186_1_MdR.root",
  sampleBaseDir+"/pat/PATtuple_187_1_jf8.root",
  sampleBaseDir+"/pat/PATtuple_188_1_jr5.root",
  sampleBaseDir+"/pat/PATtuple_189_1_QM6.root",
  sampleBaseDir+"/pat/PATtuple_190_1_lOA.root",
  sampleBaseDir+"/pat/PATtuple_191_1_iGc.root",
  sampleBaseDir+"/pat/PATtuple_192_1_pHG.root",
  sampleBaseDir+"/pat/PATtuple_193_1_F6P.root",
  sampleBaseDir+"/pat/PATtuple_194_1_nag.root",
  sampleBaseDir+"/pat/PATtuple_195_1_P2c.root",
  sampleBaseDir+"/pat/PATtuple_196_1_yEM.root",
  sampleBaseDir+"/pat/PATtuple_197_1_Lam.root",
  sampleBaseDir+"/pat/PATtuple_198_1_EeA.root",
  sampleBaseDir+"/pat/PATtuple_199_1_7EU.root",
  sampleBaseDir+"/pat/PATtuple_200_1_Vk7.root",
  sampleBaseDir+"/pat/PATtuple_201_1_LcO.root",
  sampleBaseDir+"/pat/PATtuple_202_1_eqC.root",
  sampleBaseDir+"/pat/PATtuple_203_1_wge.root",
  sampleBaseDir+"/pat/PATtuple_204_1_LVM.root",
  sampleBaseDir+"/pat/PATtuple_205_1_r1d.root",
  sampleBaseDir+"/pat/PATtuple_206_1_83v.root",
  sampleBaseDir+"/pat/PATtuple_207_1_TJ3.root",
  sampleBaseDir+"/pat/PATtuple_208_1_7LB.root",
  sampleBaseDir+"/pat/PATtuple_209_1_Ykp.root",
  sampleBaseDir+"/pat/PATtuple_210_1_i2H.root",
  sampleBaseDir+"/pat/PATtuple_211_1_84m.root",
  sampleBaseDir+"/pat/PATtuple_212_1_pnO.root",
  sampleBaseDir+"/pat/PATtuple_213_1_zOT.root",
  sampleBaseDir+"/pat/PATtuple_214_1_VBc.root",
  sampleBaseDir+"/pat/PATtuple_215_1_KnD.root",
  sampleBaseDir+"/pat/PATtuple_216_1_dWa.root",
  sampleBaseDir+"/pat/PATtuple_217_1_SCM.root",
  sampleBaseDir+"/pat/PATtuple_218_1_N5s.root",
  sampleBaseDir+"/pat/PATtuple_219_1_E8z.root",
  sampleBaseDir+"/pat/PATtuple_220_1_dwc.root",
  sampleBaseDir+"/pat/PATtuple_221_1_IWn.root",
  sampleBaseDir+"/pat/PATtuple_222_1_aFS.root",
  sampleBaseDir+"/pat/PATtuple_223_1_18t.root",
  sampleBaseDir+"/pat/PATtuple_224_0_7gw.root",
  sampleBaseDir+"/pat/PATtuple_225_0_XMu.root",
  sampleBaseDir+"/pat/PATtuple_226_0_WXH.root",
  sampleBaseDir+"/pat/PATtuple_227_0_Pwm.root",
  sampleBaseDir+"/pat/PATtuple_228_0_MAw.root",
  sampleBaseDir+"/pat/PATtuple_229_0_Dz7.root",
  sampleBaseDir+"/pat/PATtuple_230_0_SpO.root",
  sampleBaseDir+"/pat/PATtuple_231_0_csY.root",
  sampleBaseDir+"/pat/PATtuple_232_0_RhD.root",
  sampleBaseDir+"/pat/PATtuple_233_0_wPz.root",
  sampleBaseDir+"/pat/PATtuple_234_0_BQ8.root",
  sampleBaseDir+"/pat/PATtuple_235_0_n5N.root",
  sampleBaseDir+"/pat/PATtuple_236_0_gKK.root",
  sampleBaseDir+"/pat/PATtuple_237_0_EaA.root",
  sampleBaseDir+"/pat/PATtuple_238_0_j5t.root",
  sampleBaseDir+"/pat/PATtuple_239_0_Rkg.root",
  sampleBaseDir+"/pat/PATtuple_240_0_hCH.root",
  sampleBaseDir+"/pat/PATtuple_241_0_ba2.root",
  sampleBaseDir+"/pat/PATtuple_242_0_nzE.root",
  sampleBaseDir+"/pat/PATtuple_243_0_NHx.root",
  sampleBaseDir+"/pat/PATtuple_244_0_Pot.root",
  sampleBaseDir+"/pat/PATtuple_245_0_Df9.root",
  sampleBaseDir+"/pat/PATtuple_246_0_5W8.root",
  sampleBaseDir+"/pat/PATtuple_247_0_X54.root",
  sampleBaseDir+"/pat/PATtuple_248_0_u7G.root",
  sampleBaseDir+"/pat/PATtuple_249_0_bvh.root",
  sampleBaseDir+"/pat/PATtuple_250_0_Lt9.root",
  sampleBaseDir+"/pat/PATtuple_251_0_hrC.root",
  sampleBaseDir+"/pat/PATtuple_252_0_bFt.root",
  sampleBaseDir+"/pat/PATtuple_253_0_ksV.root",
  sampleBaseDir+"/pat/PATtuple_254_0_bJT.root",
  sampleBaseDir+"/pat/PATtuple_255_0_h0b.root",
  sampleBaseDir+"/pat/PATtuple_256_0_gkn.root",
  sampleBaseDir+"/pat/PATtuple_257_0_CKo.root",
  sampleBaseDir+"/pat/PATtuple_258_0_TZB.root",
  sampleBaseDir+"/pat/PATtuple_259_0_hEC.root",
  sampleBaseDir+"/pat/PATtuple_260_0_iLv.root",
  sampleBaseDir+"/pat/PATtuple_261_0_anr.root",
  sampleBaseDir+"/pat/PATtuple_262_0_GaO.root",
  sampleBaseDir+"/pat/PATtuple_263_0_jz3.root",
  sampleBaseDir+"/pat/PATtuple_264_0_dtC.root",
  sampleBaseDir+"/pat/PATtuple_265_0_Gyg.root",
  sampleBaseDir+"/pat/PATtuple_266_0_poD.root",
  sampleBaseDir+"/pat/PATtuple_267_0_hpS.root",
  sampleBaseDir+"/pat/PATtuple_268_0_eAR.root",
  sampleBaseDir+"/pat/PATtuple_269_0_sPS.root",
  sampleBaseDir+"/pat/PATtuple_270_0_ehy.root",
  sampleBaseDir+"/pat/PATtuple_271_0_fA2.root",
  sampleBaseDir+"/pat/PATtuple_272_0_DiZ.root",
  sampleBaseDir+"/pat/PATtuple_273_0_zBL.root",
  sampleBaseDir+"/pat/PATtuple_274_0_c6A.root",
  sampleBaseDir+"/pat/PATtuple_275_0_v1J.root",
  sampleBaseDir+"/pat/PATtuple_276_0_kGO.root",
  sampleBaseDir+"/pat/PATtuple_277_0_CNq.root",
  sampleBaseDir+"/pat/PATtuple_278_0_yPC.root",
  sampleBaseDir+"/pat/PATtuple_279_0_5zq.root",
  sampleBaseDir+"/pat/PATtuple_280_0_CCS.root",
  sampleBaseDir+"/pat/PATtuple_281_0_xQe.root",
  sampleBaseDir+"/pat/PATtuple_282_0_hEy.root",
  sampleBaseDir+"/pat/PATtuple_283_0_mT9.root",
  sampleBaseDir+"/pat/PATtuple_284_0_qYZ.root",
  sampleBaseDir+"/pat/PATtuple_285_0_ERD.root",
  sampleBaseDir+"/pat/PATtuple_286_0_WZr.root",
  sampleBaseDir+"/pat/PATtuple_287_0_0O0.root",
  sampleBaseDir+"/pat/PATtuple_288_0_WAV.root",
  sampleBaseDir+"/pat/PATtuple_289_0_OMa.root",
  sampleBaseDir+"/pat/PATtuple_290_0_AR1.root",
  sampleBaseDir+"/pat/PATtuple_291_0_38o.root",
  sampleBaseDir+"/pat/PATtuple_292_0_ouV.root",
  sampleBaseDir+"/pat/PATtuple_293_0_j5p.root",
  sampleBaseDir+"/pat/PATtuple_294_0_xaO.root",
  sampleBaseDir+"/pat/PATtuple_295_0_Sy6.root",
  sampleBaseDir+"/pat/PATtuple_296_0_cd5.root",
  sampleBaseDir+"/pat/PATtuple_297_0_J4S.root",
  sampleBaseDir+"/pat/PATtuple_298_0_NEJ.root",
  sampleBaseDir+"/pat/PATtuple_299_0_YH5.root",
  sampleBaseDir+"/pat/PATtuple_300_0_r10.root",
  sampleBaseDir+"/pat/PATtuple_301_0_D26.root",
  sampleBaseDir+"/pat/PATtuple_302_0_UQy.root",
  sampleBaseDir+"/pat/PATtuple_303_0_UGP.root",
  sampleBaseDir+"/pat/PATtuple_304_0_DoR.root",
  sampleBaseDir+"/pat/PATtuple_305_0_YHP.root",
  sampleBaseDir+"/pat/PATtuple_306_0_yZq.root",
  sampleBaseDir+"/pat/PATtuple_307_0_NSR.root",
  sampleBaseDir+"/pat/PATtuple_308_0_zOE.root",
  sampleBaseDir+"/pat/PATtuple_309_0_8Bf.root",
  sampleBaseDir+"/pat/PATtuple_310_0_V2Q.root",
  sampleBaseDir+"/pat/PATtuple_311_0_Fnh.root",
  sampleBaseDir+"/pat/PATtuple_312_0_0NC.root",
  sampleBaseDir+"/pat/PATtuple_313_0_wES.root",
  sampleBaseDir+"/pat/PATtuple_314_0_d8Z.root",
  sampleBaseDir+"/pat/PATtuple_315_0_TVY.root",
  sampleBaseDir+"/pat/PATtuple_316_0_Kaw.root",
  sampleBaseDir+"/pat/PATtuple_317_0_oIS.root",
  sampleBaseDir+"/pat/PATtuple_318_0_AMo.root",
  sampleBaseDir+"/pat/PATtuple_319_0_8DF.root",
  sampleBaseDir+"/pat/PATtuple_320_0_HQi.root",
  sampleBaseDir+"/pat/PATtuple_321_0_W6N.root",
  sampleBaseDir+"/pat/PATtuple_322_0_obe.root",
  sampleBaseDir+"/pat/PATtuple_323_0_fJL.root",
  sampleBaseDir+"/pat/PATtuple_324_0_qbO.root",
  sampleBaseDir+"/pat/PATtuple_325_0_jCY.root",
  sampleBaseDir+"/pat/PATtuple_326_0_nbH.root",
  sampleBaseDir+"/pat/PATtuple_327_0_Vy3.root",
  sampleBaseDir+"/pat/PATtuple_328_0_Qsb.root",
  sampleBaseDir+"/pat/PATtuple_329_0_cqo.root",
  sampleBaseDir+"/pat/PATtuple_330_0_Z6A.root",
  sampleBaseDir+"/pat/PATtuple_331_0_18S.root",
  sampleBaseDir+"/pat/PATtuple_332_0_B5U.root",
  sampleBaseDir+"/pat/PATtuple_333_0_NDa.root",
  sampleBaseDir+"/pat/PATtuple_334_0_K3k.root",
  sampleBaseDir+"/pat/PATtuple_335_0_PD7.root",
  sampleBaseDir+"/pat/PATtuple_336_0_Cyx.root",
  sampleBaseDir+"/pat/PATtuple_337_0_0pY.root",
  sampleBaseDir+"/pat/PATtuple_338_0_gsM.root",
  sampleBaseDir+"/pat/PATtuple_339_0_MV7.root",
  sampleBaseDir+"/pat/PATtuple_340_0_4YA.root",
  sampleBaseDir+"/pat/PATtuple_341_0_ik1.root",
  sampleBaseDir+"/pat/PATtuple_342_0_brj.root",
  sampleBaseDir+"/pat/PATtuple_343_0_3aI.root",
  sampleBaseDir+"/pat/PATtuple_344_0_yHA.root",
  sampleBaseDir+"/pat/PATtuple_345_0_RTj.root",
  sampleBaseDir+"/pat/PATtuple_346_0_Hhk.root",
  sampleBaseDir+"/pat/PATtuple_347_0_Teu.root",
  sampleBaseDir+"/pat/PATtuple_348_0_4kn.root",
  sampleBaseDir+"/pat/PATtuple_349_0_3kq.root",
  sampleBaseDir+"/pat/PATtuple_350_0_SgH.root",
  sampleBaseDir+"/pat/PATtuple_351_0_vtS.root",
  sampleBaseDir+"/pat/PATtuple_352_0_C8M.root",
  sampleBaseDir+"/pat/PATtuple_353_0_Ddf.root",
  sampleBaseDir+"/pat/PATtuple_354_0_x5g.root",
  sampleBaseDir+"/pat/PATtuple_355_0_Coi.root",
  sampleBaseDir+"/pat/PATtuple_356_0_dg2.root",
  sampleBaseDir+"/pat/PATtuple_357_0_rDd.root",
  sampleBaseDir+"/pat/PATtuple_358_0_wzM.root",
  sampleBaseDir+"/pat/PATtuple_359_0_Z4K.root",
  sampleBaseDir+"/pat/PATtuple_360_0_S03.root",
  sampleBaseDir+"/pat/PATtuple_361_0_Rnh.root",
  sampleBaseDir+"/pat/PATtuple_362_0_JzA.root",
  sampleBaseDir+"/pat/PATtuple_363_0_YPl.root",
  sampleBaseDir+"/pat/PATtuple_364_0_dQl.root",
  sampleBaseDir+"/pat/PATtuple_365_0_4Zf.root",
  sampleBaseDir+"/pat/PATtuple_366_0_Rmw.root",
  sampleBaseDir+"/pat/PATtuple_367_0_eKy.root",
  sampleBaseDir+"/pat/PATtuple_368_0_Eqz.root",
  sampleBaseDir+"/pat/PATtuple_369_0_FUL.root",
  sampleBaseDir+"/pat/PATtuple_370_0_RZM.root",
  sampleBaseDir+"/pat/PATtuple_371_0_zvN.root",
  sampleBaseDir+"/pat/PATtuple_372_0_icP.root",
  sampleBaseDir+"/pat/PATtuple_373_0_cp0.root",
  sampleBaseDir+"/pat/PATtuple_374_0_gnJ.root",
  sampleBaseDir+"/pat/PATtuple_375_0_HTv.root",
  sampleBaseDir+"/pat/PATtuple_376_0_aav.root",
  sampleBaseDir+"/pat/PATtuple_377_0_AU2.root",
  sampleBaseDir+"/pat/PATtuple_378_0_gEp.root",
  sampleBaseDir+"/pat/PATtuple_379_0_Vzh.root",
  sampleBaseDir+"/pat/PATtuple_380_0_xYc.root",
  sampleBaseDir+"/pat/PATtuple_381_0_9tS.root",
  sampleBaseDir+"/pat/PATtuple_382_0_sWz.root",
  sampleBaseDir+"/pat/PATtuple_383_0_u5U.root",
  sampleBaseDir+"/pat/PATtuple_384_0_mXS.root",
  sampleBaseDir+"/pat/PATtuple_385_0_9V7.root",
  sampleBaseDir+"/pat/PATtuple_386_0_Ywo.root",
  sampleBaseDir+"/pat/PATtuple_387_0_Q0J.root",
  sampleBaseDir+"/pat/PATtuple_388_0_vAb.root",
  sampleBaseDir+"/pat/PATtuple_389_0_Zyd.root",
  sampleBaseDir+"/pat/PATtuple_390_0_PXY.root",
  sampleBaseDir+"/pat/PATtuple_391_0_nBs.root",
  sampleBaseDir+"/pat/PATtuple_392_0_n3g.root",
  sampleBaseDir+"/pat/PATtuple_393_0_M3K.root",
  sampleBaseDir+"/pat/PATtuple_394_0_I8s.root",
  sampleBaseDir+"/pat/PATtuple_395_0_AF6.root",
  sampleBaseDir+"/pat/PATtuple_396_0_rEt.root",
  sampleBaseDir+"/pat/PATtuple_397_0_9uB.root",
  sampleBaseDir+"/pat/PATtuple_398_0_oLN.root",
  sampleBaseDir+"/pat/PATtuple_399_0_Y0q.root",
  sampleBaseDir+"/pat/PATtuple_400_0_YYF.root",
  sampleBaseDir+"/pat/PATtuple_401_0_FYy.root",
  sampleBaseDir+"/pat/PATtuple_402_0_xwJ.root",
  sampleBaseDir+"/pat/PATtuple_403_0_M5d.root",
  sampleBaseDir+"/pat/PATtuple_404_0_Pzz.root",
  sampleBaseDir+"/pat/PATtuple_405_0_LGD.root",
  sampleBaseDir+"/pat/PATtuple_406_0_Wfv.root"
]

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "MC"
sampleRunMu = 0
