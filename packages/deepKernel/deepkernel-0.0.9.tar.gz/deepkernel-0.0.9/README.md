20250926 0.0.5 正式第一版，主要使用configuration.init、input.open_job、information.get_profile_box以测试SDK包是否可用

20250928 0.0.7 正式第二版，主要加入output模块用以测试导出Gerber/ODBPP接口是否可用，验证导出目前不可使用

20250929 0.0.8 正式第三版，information模块中加入get_layer_feature_count与get_all_features_info为在无法导出时测试验证导入的正确性、在导入后获取信息、目前已经确认可以使用information模块的导出函数获取所有feature信息但是无法使用output模块的导出函数输出目标文件

20250929 0.0.9 正式第四版，input、output、base模块加入了dxf的导入导出函数，用于测试
