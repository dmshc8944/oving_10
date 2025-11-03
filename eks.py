from data import emner
from lig_til_emne import legg_til_emne_i_studieplan, vis_studieplan
from emne import Emne

# Создаем предметы
emner.append(Emne("INF100", "Innføring i programmering", "H", 10))
emner.append(Emne("MAT110", "Grunnkurs i matematikk", "V", 10))

# Добавляем в план
legg_til_emne_i_studieplan(emner[0], 1)
legg_til_emne_i_studieplan(emner[1], 2)

# Показываем план
vis_studieplan()
