#### 环境要求：

- `win10`或`ubuntu16.04`

- `python3.6.12`

- `cpu`

- `tensorflow==1.6.0`
- 先安装`sonnet`再卸载，我也不知道为什么，反正就得这样，估计有些依赖包需求

- `dm-sonney==2.0.0`
- `matplotlib==3.3.2`
- `Django==3.1.2`
- `numpy==1.19.0`
- 裸机建议先安装`anaconda3`，再在虚拟环境下运行，省心

#### 本地运行：

- `git clone`我的项目
- 从[codeocean](https://codeocean.com/capsule/5723040/tree/v1)下载`savedModels.zip`解压到`deepcube/code/savedModels`
- 导航到`README.md`当前文件夹下，运行`python manage.py runserver`，可以在本地`http://127.0.0.1:8000/deepcube`访问网页并运行、求解
- 运行`python manage.py runserver 0.0.0.0:8000`可以外网访问本机(你的电脑)`IP`的`8000`端口，即`url=http://IP:8000/deepcube`，不过要先修改`Cube/setting.py`的`ALLOWED_HOSTS=["IP1","IP2","127.0.0.1",]`

#### 外网`url`

- `http://167.179.64.188:8000/deepcube`

[GitHub](https://github.com/OPilgrim/DeepCube)

# 注意：由于经费有限，服务器只能提供一个月的服务，即11.16就会停止服务，所以外网测试需尽早进行，否则无法体验