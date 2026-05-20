with prepare_task_start_end as (
    select serial_id, time as prepare_start, update_time as prepare_end
    from feature_on.feature_task
    where stage = 'anti_neo' and time >= unix_timestamp(current_date - 3)
),
     feature_task_start_end as (
         select serial_id, time as feature_start, update_time as feature_end
         from feature_on.feature_task
         where stage = 'model' and time >= unix_timestamp(current_date - 3)
     ),
     model_task_start_end as (
         select serial_id, time as model_start, update_time as model_end
         from feature_on.feature_task
         where stage = 'model_check' and time >= unix_timestamp(current_date - 3)
     ),
     total_start_end as (
         select time as total_start, update_time total_end, serial_id, update_time - time diff
         from ods.user_product_relation
         where time >= unix_timestamp(current_date - 3) and serial_id != 0 order by diff desc
     ),
     base_order as (
         select serial_id, loan_type, create_time
         from ods.virtual_loan pre
         where create_time >= unix_timestamp(current_date - 3) and create_time < unix_timestamp(current_date)
     ),
     tmp_data as (
         select t1.serial_id,
                loan_type,
                to_timestamp(create_time)::date as snap_date,
                total_end - total_start         as total_diff,
                prepare_end - prepare_start     as prepare_diff,
                feature_end - prepare_end       as feature_diff,
                model_end - feature_end         as model_diff
         from base_order t1
                  left join total_start_end t2 on t1.serial_id = t2.serial_id
                  left join prepare_task_start_end t3 on t1.serial_id = t3.serial_id
                  left join feature_task_start_end t4 on t1.serial_id = t4.serial_id
                  left join model_task_start_end t5 on t1.serial_id = t5.serial_id
         where total_start>0 and total_end>0 and prepare_start>0 and prepare_end>0 and feature_start>0 and feature_end>0 and model_start>0 and model_end>0
     ),
         select snap_date,
                loan_type,
                count(distinct serial_id)                                         total_cnt,
                sum(total_diff)                                                   total_s,
                count(distinct case when total_diff > 30 then serial_id end)   as shouxin_more_than_30s,
                count(distinct case when total_diff > 60 then serial_id end)   as shouxin_more_than_60s,
                sum(prepare_diff)                                                 total_prepare_s,
                count(distinct case when prepare_diff > 30 then serial_id end) as prepare_more_than_30s,
                count(distinct case when prepare_diff > 60 then serial_id end) as prepare_more_than_60s,
                sum(feature_diff)                                              as total_feature_s,
                count(distinct case when feature_diff > 30 then serial_id end) as feature_more_than_30s,
                count(distinct case when feature_diff > 60 then serial_id end) as feature_more_than_60s,
                sum(model_diff)                                                as total_model_s,
                count(distinct case when model_diff > 30 then serial_id end)   as model_more_than_30s,
                count(distinct case when model_diff > 60 then serial_id end)   as model_more_than_60s,
                max(total_diff)                                                as max_total_diff_s,
                max(prepare_diff)                                              as max_prepare_diff_s,
                max(feature_diff)                                              as max_feature_diff_s,
                max(model_diff)                                                as max_model_diff_s
         from tmp_data
         group by 1, 2