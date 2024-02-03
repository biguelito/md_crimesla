select 
	dtc.Crime_Desc 
	, count(dtc.Id_CrimeTipo)
from 
	fato_vitima fv
	inner join dim_tipo_crime dtc  
		on dtc.Id_CrimeTipo  = fv.Id_CrimeTipo 
	inner join dim_local_crime dlc 
		on dlc.Id_Local = fv.Id_Local 
	inner join dim_data dd 
		on dd.keyData = fv.Id_Data_Ocorrencia 
where 1=1
	and %s <= dd.data_id -- data minima da procura
	and dd.data_id <= %s -- data maxima da procura 
	-- and dac.Arma_Usada_Cd <> 500 -- removendo arma desconhecida
	and dlc.Area in (#areas#) -- lista de codigos de areas
group by
	dtc.Id_CrimeTipo 
	, dtc.Crime_Desc 
order by 
	count(dtc.Id_CrimeTipo) desc
	, dtc.Crime_Desc 