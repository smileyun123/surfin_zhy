
[//]: # (1、订单授信表) virtual_loan

[//]: # (2、放款表) loan --整期
[//]: # (3、还款表) repayment_plan --分期
[//]: # (3、还款表) repayment_plan --分期



select *, from_unixtime(time) as '本地时间', from_unixtime(time +50400) as '北京时间', (update_time-time) from feature_compute_stat where (update_time-time) > 10 order by id desc limit 50;

1. 
2. 检查app数据源 
select * from app_install_upgrade_time_record where  user_id = 250890 and code=7100 and status=6 and create_time <=1723960551 and create_time >=(1723960551-365*86400);
4. 



with prepare_task_start_end as (
    select serial_id, time as prepare_start, update_time as prepare_end
    from feature_on.feature_task
    where stage = 'anti_neo'
      and time >= (date_part('epoch',current_date - 3))::integer
),
     feature_task_start_end as (
         select serial_id, time as feature_start, update_time as feature_end
         from feature_on.feature_task
         where stage = 'model'
           and time >= (date_part('epoch',current_date - 3))::integer
     ),
     model_task_start_end as (
         select serial_id, time as model_start, update_time as model_end
         from feature_on.feature_task
         where stage = 'model_check'
           and time >= (date_part('epoch',current_date - 3))::integer
     ),
     total_start_end as (
        select  MIN(time) as total_start,max(update_time)  as total_end,serial_id, user_id,max(update_time)-min(time) diff
        from feature_on.feature_task
        where time>= (date_part('epoch',current_date - 3))::integer
        and serial_id > 0
        and stage in ('anti_neo','model_check')
        GROUP BY serial_id,user_id
        order by diff desc

     ),base_order as (
         select serial_id, loan_type, create_time
         from ods.virtual_loan pre
         where create_time >= (date_part('epoch',current_date - 3))::integer
           and create_time < (date_part('epoch',current_date ))::integer
     )
   select t1.serial_id,
                loan_type,
                to_timestamp(create_time)::date as snap_date,
                total_end - total_start         as total_diff,   --授信算时间
                feature_end - prepare_end       as feature_diff, --特征计算时间
                model_end - feature_end         as model_diff    --模型计算时间
         from base_order t1
                  left join total_start_end t2 on t1.serial_id = t2.serial_id
                  left join prepare_task_start_end t3 on t1.serial_id = t3.serial_id
                  left join feature_task_start_end t4 on t1.serial_id = t4.serial_id
                  left join model_task_start_end t5 on t1.serial_id = t5.serial_id
         where total_start>0 and total_end>0 and prepare_start>0 and prepare_end>0
           and feature_start>0 and feature_end>0 and model_start>0 and model_end>0