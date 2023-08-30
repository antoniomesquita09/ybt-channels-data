select * from channels;

-- Total de inscritos por país
select abbreviation, sum(subscribers) as total_subs
from channels
group by abbreviation
order by total_subs desc;

-- Total de visualizações de vídeos por país
select abbreviation, sum(video_views) as total_views
from channels
group by abbreviation
order by total_views desc;

-- Valores recebidos (mês) por canal
select youtuber, abbreviation, highest_monthly_earnings::float8::numeric::money
from channels
order by highest_monthly_earnings desc;

-- Valores recebidos (ano) por canal
select youtuber, abbreviation, highest_yearly_earnings::float8::numeric::money
from channels
order by highest_monthly_earnings desc;

-- Média de valores recebidos por país
select abbreviation, count(*) as total_channels, avg(highest_monthly_earnings)::float8::numeric::money as highest_monthly_earnings_avg
from channels
group by abbreviation
having count(*) > 10
order by highest_monthly_earnings_avg desc;