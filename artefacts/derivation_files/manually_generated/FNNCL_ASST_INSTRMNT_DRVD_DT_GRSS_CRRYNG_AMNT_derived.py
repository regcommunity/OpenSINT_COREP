from django.db import models
from pybirdai.annotations.decorators import lineage

class FNNCL_ASST_INSTRMNT_DRVD_DT(models.Model):

    @property
    @lineage(dependencies={'BIRD_FNNCL_ASST_INSTRMNT_DRVD_DT.PRFRMNG_STTS', 'BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.ACCNTNG_CLSSFCTN', 'BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.ACCMLTD_IMPRMNT', 'BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.CRRYNG_AMNT', 'BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.IMPRMNT_STTS', 'FR_VLD_BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.ACCMLTD_CHNGS_FV', 'FR_VLD_BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.FV', 'BBLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_NGAAP.GNRL_ALLWNCS_BNK_RSK', 'BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_NGAAP.GNRL_ALLWNCS_CRDT_RSK', 'FNNCL_ASST_INSTRMNT.SBJCT_IMPRMNT_INDCTR'})
    def GRSS_CRRYNG_AMNT(self):
        accntng_clssfctn = None
        accmltd_imprmnt = 0
        accmltd_chngs_fv_cr = 0
        crryng_amnt = 0
        fv = 0
        gnrl_allwncs_bnk_rsk = 0
        gnrl_allwncs_crdt_rsk = 0
        prfrmng_stts = self.PRFRMNG_STTS
        imprmnt_stts = None
        sbjct_imprmnt_idctr = None
        if not self.Financial_asset_instrument_has_Financial_asset_instrument_derived_data is None:
            sbjct_imprmnt_idctr = self.Financial_asset_instrument_has_Financial_asset_instrument_derived_data.SBJCT_IMPRMNT_INDCTR
            financial_asset_type = self.Financial_asset_instrument_has_Financial_asset_instrument_derived_data.Financial_asset_instrument_type_delegate
            if financial_asset_type.blnc_sht_rcgnsd_fnncl_asst_instrmnt:
                accntng_clssfctn = financial_asset_type.blnc_sht_rcgnsd_fnncl_asst_instrmnt.ACCNTNG_CLSSFCTN
                accmltd_imprmnt = financial_asset_type.blnc_sht_rcgnsd_fnncl_asst_instrmnt.ACCMLTD_IMPRMNT
                crryng_amnt = financial_asset_type.blnc_sht_rcgnsd_fnncl_asst_instrmnt.CRRYNG_AMNT
                imprmnt_stts = financial_asset_type.blnc_sht_rcgnsd_fnncl_asst_instrmnt.IMPRMNT_STTS
                balance_sheet_recognised_financial_asset_instrument_by_fair_value_type = financial_asset_type.blnc_sht_rcgnsd_fnncl_asst_instrmnt.Balance_sheet_recognised_financial_asset_instrument_by_fair_value_type_delegate
                if not balance_sheet_recognised_financial_asset_instrument_by_fair_value_type is None:
                    if hasattr(balance_sheet_recognised_financial_asset_instrument_by_fair_value_type, 'fr_vld_blnc_sht_rcgnsd_fnncl_asst_instrmnt'):
                        if balance_sheet_recognised_financial_asset_instrument_by_fair_value_type.fr_vld_blnc_sht_rcgnsd_fnncl_asst_instrmnt:
                            accmltd_chngs_fv_cr = balance_sheet_recognised_financial_asset_instrument_by_fair_value_type.fr_vld_blnc_sht_rcgnsd_fnncl_asst_instrmnt.ACCMLTD_CHNGS_FV
                            fv = balance_sheet_recognised_financial_asset_instrument_by_fair_value_type.fr_vld_blnc_sht_rcgnsd_fnncl_asst_instrmnt.FV
                balance_sheet_recognised_financial_asset_instrument_type = financial_asset_type.blnc_sht_rcgnsd_fnncl_asst_instrmnt.Balance_sheet_recognised_financial_asset_instrument_type_delegate
                if not balance_sheet_recognised_financial_asset_instrument_type is None:
                    if hasattr(balance_sheet_recognised_financial_asset_instrument_type, 'blnc_sht_rcgnsd_fnncl_asst_instrmnt_ngaap'):
                        if balance_sheet_recognised_financial_asset_instrument_type.blnc_sht_rcgnsd_fnncl_asst_instrmnt_ngaap:
                            gnrl_allwncs_bnk_rsk = balance_sheet_recognised_financial_asset_instrument_type.GNRL_ALLWNCS_BNK_RSK
                            gnrl_allwncs_crdt_rsk = balance_sheet_recognised_financial_asset_instrument_type.GNRL_ALLWNCS_CRDT_RSK
        return_grss_crryng_amnt = 0
        match accntng_clssfctn:
            case '4' | '41' | '47' | '7':
                match prfrmng_stts:
                    case '11':
                        return_grss_crryng_amnt = fv
                    case '1':
                        return_grss_crryng_amnt = fv + accmltd_chngs_fv_cr
                    case _:
                        return_grss_crryng_amnt = 0
            case '6' | '8' | '9':
                return_grss_crryng_amnt = crryng_amnt - accmltd_imprmnt
            case '77':
                match imprmnt_stts:
                    case '26':
                        return_grss_crryng_amnt = crryng_amnt - accmltd_imprmnt
                    case '211':
                        return_grss_crryng_amnt = crryng_amnt - gnrl_allwncs_crdt_rsk
                    case '212':
                        return_grss_crryng_amnt = crryng_amnt - gnrl_allwncs_bnk_rsk
                    case _:
                        return_grss_crryng_amnt = 0
            case '9':
                match sbjct_imprmnt_idctr:
                    case '1':
                        match prfrmng_stts:
                            case '26':
                                return_grss_crryng_amnt = crryng_amnt - accmltd_imprmnt
                            case '211':
                                return_grss_crryng_amnt = crryng_amnt - gnrl_allwncs_crdt_rsk
                            case '212':
                                return_grss_crryng_amnt = crryng_amnt - gnrl_allwncs_bnk_rsk
                            case _:
                                return_grss_crryng_amnt = 0
                    case '2':
                        match prfrmng_stts:
                            case '11':
                                return_grss_crryng_amnt = fv
                            case '1':
                                return_grss_crryng_amnt = fv + accmltd_chngs_fv_cr
                            case _:
                                return_grss_crryng_amnt = 0
                    case _:
                        return_grss_crryng_amnt = 0
            case '76' | '73':
                return_grss_crryng_amnt = crryng_amnt
            case '74':
                return_grss_crryng_amnt = crryng_amnt + accmltd_imprmnt
            case '2' | '3':
                return_grss_crryng_amnt = fv
            case _:
                return_grss_crryng_amnt = 0
        return return_grss_crryng_amnt

    class Meta:
        pass