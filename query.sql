Select max(high) as Hourly_high,name,DATE_TRUNC('hour',date_parse(myh_yf_streamdata.ts, '%Y-%m-%d %H:%i:%s'))as hour
From myh_yf_streamdata
group by name,DATE_TRUNC('hour',date_parse(myh_yf_streamdata.ts, '%Y-%m-%d %H:%i:%s'))
order by name,DATE_TRUNC('hour',date_parse(myh_yf_streamdata.ts, '%Y-%m-%d %H:%i:%s')) asc
