from enum import Enum


class CultivationEnum(Enum):
    SOJA = "Soja"
    MILHO = "Milho"
    ALGODAO = "Algodão"
    CAFE = "Café"
    CANA_DE_ACUCAR = "Cana de Açucar"


if __name__ == '__main__':
    cultivation = [CultivationEnum[cultivation.name].value for cultivation in CultivationEnum]

    if not cultivation.__contains__("Soja"):
        print("aaaaaa")



# 103,17