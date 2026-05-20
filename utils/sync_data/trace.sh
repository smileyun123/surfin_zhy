#!/bin/bash
# 传入回溯天数
back_day=$1
#job_table=("ke_credolab_v1_fea_on_off" "ke_credolab_v2_fea_on_off")
fea_name=$2
job_table=($fea_name)

export PYTHONPATH=/data1/work/zhy/Global
#export off_kaby=true
#export model_name=KkLimitXgboost101Dpd7
#export off_mode=partial   增量同步，若有需要可以打开
#export off_loan_type=2
#export off_status_limit="578"
#export MALLOC_MMAP_THRESHOLD_=65536
#export MALLOC_MMAP_THRESHOLD_=8192
#export MALLOC_MMAP_THRESHOLD_=4096
#export LD_PRELOAD="/usr/lib/libtcmalloc.so"
#export LD_PRELOAD="/usr/lib64/libjemalloc.so.1"
#export allowed_serial_path='/data1/work/zhy/Global/files/buro_one.csv'

# 更改可传参的回溯时间
function  reanme_time()
{
    sed -i "s/(datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d 00:00:00')/sys.argv[1]/g"  ./bin/$1.py
    sed -i "s/datetime.datetime.now().strftime('%Y-%m-%d 00:00:00')/sys.argv[2]/g"  ./bin/$1.py
}
# 跑任务
function start_job()
{
    step=0
    for((i=0;i<=$(($2));i+=1))
    do
        echo "i=$(i)"
        let step+=1
        j=$(($i+1))
        #end_tm=`date +"%Y-%m-%d 00:00:00" -d "-$i""day"`
        #begin_tm=`date +"%Y-%m-%d 00:00:00" -d "-$j""day"`
        end_tm=`date +"%Y-%m-%d 00:00:00" -d "-$i""day"`
        begin_tm=`date +"%Y-%m-%d 00:00:00" -d "-$j""day"`
        python ./bin/$1.py "$begin_tm" "$end_tm" > ./logs/out.$1 2>&1 &
#        echo $1.py "$begin_tm" "$end_tm"
        if [ $step -eq 1 ] ; then
            step=0
            wait
        fi
    done
}

for job_name in ${job_table[@]};
do
    # 重命名
    reanme_time $job_name
    # 跑任务
    start_job $job_name $back_day
done
#wait
#python  bin/send_job_msg.py "$2 数回溯完成"
