select 
	dac.Arma_Desc 
	, count(dac.Id_Arma)
from 
	fato_vitima fv
	inner join dim_arma_crime dac 
		on dac.Id_Arma = fv.Id_Arma
	inner join dim_local_crime dlc 
		on dlc.Id_Local = fv.Id_Local 
	inner join dim_data dd 
		on dd.keyData = fv.Id_Data_Ocorrencia 
where 1=1
	and %s <= dd.data_id -- data minima da procura
	and dd.data_id <= %s -- data maxima da procura 
	and dac.Arma_Usada_Cd <> 500 -- removendo arma desconhecida
	#usarareas#and dlc.Area in (#areas#) -- lista de codigos de areas
group by
	dac.Id_Arma 
	, dac.Arma_Desc 
order by 
	count(dac.Id_Arma) desc
	, dac.Arma_Desc
