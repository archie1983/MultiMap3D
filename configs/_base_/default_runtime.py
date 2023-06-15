#default_scope = 'mmdet3d'
#
#default_hooks = dict(
#    timer=dict(type='IterTimerHook'),
#    logger=dict(type='LoggerHook', interval=50),
#    param_scheduler=dict(type='ParamSchedulerHook'),
#    checkpoint=dict(type='CheckpointHook', interval=-1),
#    sampler_seed=dict(type='DistSamplerSeedHook'),
#    visualization=dict(type='Det3DVisualizationHook'))
#
#env_cfg = dict(
#    cudnn_benchmark=False,
#    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0),
#    dist_cfg=dict(backend='nccl'),
#)
#
#log_processor = dict(type='LogProcessor', window_size=50, by_epoch=True)
#
#log_level = 'INFO'
#load_from = None
#resume = False
#
## TODO: support auto scaling lr


#checkpoint_config = dict(interval=1)
## yapf:disable push
## By default we use textlogger hook and tensorboard
## For more loggers see
## https://mmcv.readthedocs.io/en/latest/api.html#mmcv.runner.LoggerHook
#log_config = dict(
#    interval=50,
#    hooks=[
#        dict(type='TextLoggerHook'),
#        dict(type='TensorboardLoggerHook')
#    ])
## yapf:enable
dist_params = dict(backend='nccl')
log_level = 'INFO'
work_dir = None
load_from = None
resume_from = None
workflow = [('train', 1)]
