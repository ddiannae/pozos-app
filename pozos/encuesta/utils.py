from encuesta.models import Encuesta

class RiesgoStat:

    CD_REF = 0.0005
    CR_REF = 0.003
    HG_REF = 0.0003
    MN_REF = 0.14
    AS_REF_DER = 0.0003
    AS_REF_CA = 1.5
    FLUOR_REF = 0.06

    def __init__(self, encuesta, pozo):
        self.encuesta = encuesta
        self.pozo = pozo

    ## Dosis exposición
    ## (concentracion * tasa_ingesta * FE)/peso
    ## FE = 1

    ## Cociente riesgo
    ## Dosis exposicion / dosis referencia

    def __get_riesgo(self, conc, conc_ref):
        if self.pozo[conc] is None:
            return None
        d_exp = (self.pozo[conc] * self.encuesta.total_vasos)/self.encuesta.peso
        return round(d_exp/conc_ref, 4)

    def __get_riesgo_cat(self, prop):
        if prop is None:
            return None

        if prop <= 1:
            return "bajo"
        elif prop > 1 and prop <= 3:
            return "medio"
        else:
            return "alto"

    @property
    def riesgo_cd(self):
        return self.__get_riesgo("cd_total", self.CD_REF)

    @property
    def riesgo_cr(self):
        return self.__get_riesgo("cr_total", self.CR_REF)

    @property
    def riesgo_hg(self):
        return self.__get_riesgo("hg_total", self.HG_REF)

    @property
    def riesgo_mn(self):
        return self.__get_riesgo("mn_total", self.MN_REF)

    @property
    def riesgo_as_der(self):
        return self.__get_riesgo("as_total", self.AS_REF_DER)

    @property
    def riesgo_as_ca(self):
        return self.__get_riesgo("as_total", self.AS_REF_CA)

    @property
    def riesgo_fl(self):
        return self.__get_riesgo("fluor_total", self.FLUOR_REF)

    @property
    def riesgo_cd_cat(self):
        return self.__get_riesgo_cat(self.riesgo_cd)

    @property
    def riesgo_cr_cat(self):
        return self.__get_riesgo_cat(self.riesgo_cr)

    @property
    def riesgo_hg_cat(self):
        return self.__get_riesgo_cat(self.riesgo_hg)

    @property
    def riesgo_mn_cat(self):
        return self.__get_riesgo_cat(self.riesgo_mn)

    @property
    def riesgo_as_der_cat(self):
        return self.__get_riesgo_cat(self.riesgo_as_der)

    @property
    def riesgo_as_ca_cat(self):
        return self.__get_riesgo_cat(self.riesgo_as_ca)

    @property
    def riesgo_fl_cat(self):
        return self.__get_riesgo_cat(self.riesgo_fl)
