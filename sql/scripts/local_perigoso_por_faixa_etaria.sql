select
	dlc.Localidade
	, count(dlc.Localidade)
from 
	fato_vitima fv
	inner join dim_local_crime dlc 
		on dlc.Id_Local = fv.Id_Local
	inner join dim_faixa_etaria dfe 
		on dfe.Id_faixa_etaria = fv.Id_faixa_etaria
where 
	case 
		when %s = 'Jovem' then fv.Id_faixa_etaria between 0 and 19
		when %s = 'Adulto' then fv.Id_faixa_etaria between 20 and 59
		when %s = 'Idoso' then fv.Id_faixa_etaria between 60 and 99
		else fv.Id_faixa_etaria between 0 and 99
	end
group by 
	dlc.Localidade
order by 
	count(dlc.Localidade) desc