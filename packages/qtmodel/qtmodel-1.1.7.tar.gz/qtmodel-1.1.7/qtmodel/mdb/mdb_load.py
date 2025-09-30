import json
from ..core.qt_server import QtServer
from typing import Union, List


class MdbLoad:
    """用于荷载工况荷载组和荷载组合添加"""

    # region 荷载工况与荷载组
    @staticmethod
    def add_load_case(name: str = "", case_type: str = "施工阶段荷载"):
        """
        添加荷载工况
        Args:
            name:工况名
            case_type:荷载工况类型
            _"施工阶段荷载", "恒载", "活载", "制动力", "风荷载","体系温度荷载","梯度温度荷载",
            _"长轨伸缩挠曲力荷载", "脱轨荷载", "船舶撞击荷载","汽车撞击荷载","长轨断轨力荷载", "用户定义荷载"
        Example:
            mdb.add_load_case(name="工况1",case_type="施工阶段荷载")
        Returns: 无
        """
        try:
            s = "*LOADCASE\r\n" + f"{name},{case_type}\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(f"添加荷载工况错误,{ex}")

    @staticmethod
    def add_load_group(name: str = ""):
        """
        根据荷载组名称添加荷载组
        Args:
             name: 荷载组名称
        Example:
            mdb.add_load_group(name="荷载组1")
        Returns: 无
        """
        try:
            if name != "":
                s = "*LOADGROUP\r\n" + f"{name}\r\n"
                # print(s)
            else:
                s = ""
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(f"添加荷载组,{ex}")

    @staticmethod
    def update_sink_group(name: str = "", new_name: str = "", sink: float = 0.1, node_ids: (Union[int, List[int]]) = None):
        """
        todo 更新沉降组
        Args:
             name: 沉降组名
             new_name: 新沉降组名,默认不修改
             sink: 沉降值
             node_ids: 节点编号，支持数或列表
        Example:
            mdb.update_sink_group(name="沉降1",sink=0.1,node_ids=[1,2,3])
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
            "sink": sink,
            "node_ids": node_ids,
        }
        return QtServer.send_post("UPDATE-SINK-GROUP", payload)

    @staticmethod
    def update_load_case(name: str, new_name: str = "", case_type: str = "施工阶段荷载"):
        """
        todo 更新荷载工况
        Args:
           name:工况名
           new_name:新工况名
           case_type:荷载工况类型
           _"施工阶段荷载", "恒载", "活载", "制动力", "风荷载","体系温度荷载","梯度温度荷载",
           _"长轨伸缩挠曲力荷载", "脱轨荷载", "船舶撞击荷载","汽车撞击荷载","长轨断轨力荷载", "用户定义荷载"
        Example:
           mdb.add_load_case(name="工况1",case_type="施工阶段荷载")
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
            "case_type": case_type,
        }
        return QtServer.send_post("UPDATE-LOAD-CASE", payload)

    @staticmethod
    def update_load_group(name: str, new_name: str = ""):
        """
        todo 根据荷载组名称添加荷载组
        Args:
           name: 荷载组名称
           new_name: 荷载组名称
        Example:
          mdb.update_load_group(name="荷载组1",new_name="荷载组2")
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
        }
        return QtServer.send_post("UPDATE-LOAD-GROUP", payload)

    @staticmethod
    def remove_load_case(index: int = -1, name: str = ""):
        """
        todo 删除荷载工况,参数均为默认时删除全部荷载工况
        Args:
            index:荷载编号
            name:荷载名
        Example:
            mdb.remove_load_case(index=1)
            mdb.remove_load_case(name="工况1")
            mdb.remove_load_case()
        Returns: 无
        """
        payload = {
            "index": index,
            "name": name,
        }
        return QtServer.send_post("REMOVE-LOAD-CASE", payload)

    @staticmethod
    def remove_load_group(name: str = ""):
        """
        todo 根据荷载组名称删除荷载组,参数为默认时删除所有荷载组
        Args:
             name: 荷载组名称
        Example:
            mdb.remove_load_group(name="荷载组1")
        Returns: 无
        """
        payload = {
            "name": name,
        }
        return QtServer.send_post("REMOVE-LOAD-GROUP", payload)
    # endregion

    # region 荷载组合操作
    @staticmethod
    def add_load_combine(index: int = -1, name: str = "", combine_type: int = 1, describe: str = "",
                         combine_info: list[tuple[str, str, float]] = None):
        """
        添加荷载组合
        Args:
            index:荷载组合编号
            name:荷载组合名
            combine_type:荷载组合类型 1-叠加  2-判别  3-包络 4-SRss 5-AbsSum
            describe:描述
            combine_info:荷载组合信息 [(荷载工况类型,工况名,系数)...] 工况类型如下
                _"ST"-静力荷载工况  "CS"-施工阶段荷载工况  "CB"-荷载组合
                _"MV"-移动荷载工况  "SM"-沉降荷载工况_ "RS"-反应谱工况 "TH"-时程分析
        Example:
            mdb.add_load_combine(name="荷载组合1",combine_type=1,describe="无",combine_info=[("CS","合计值",1),("CS","恒载",1)])
        Returns: 无
        """
        try:
            # if combine_info is None:
            #     combine_info = []
            # s = "*LOADCOMB\r\n" + f"NAME={name},{combine_type},{describe}\r\n"
            # s += "\r\n".join(f'{','.join(f'{x:g}' if isinstance(x, float) else str(x) for x in row)}' for row in
            #                  combine_info) + "\r\n"
            # # print(s)
            # QtServer.post_command(s, "QDAT")
            params = {
                "version": QtServer.QT_VERSION,  # 版本控制
                "index": index,
                "name": name,
                "combine_type": combine_type,
                "describe": describe,
                "combine_info": combine_info or [],
            }
            json_string = json.dumps(params, indent=2, ensure_ascii=False)
            QtServer.get_command(header="ADD-LOAD-COMBINE", command=json_string)
        except Exception as ex:
            raise Exception(f"添加荷载组合:{name}错误,{ex}")

    @staticmethod
    def remove_load_combine(index: int = -1, name: str = ""):
        """
        todo 删除荷载组合
        Args:
            index: 默认时则按照name删除荷载组合
            name:指定删除荷载组合名
        Example:
            mdb.remove_load_combine(name="荷载组合1")
        Returns: 无
        """
        payload = {
            "index": index,
            "name": name,
        }
        return QtServer.send_post("REMOVE-LOAD-COMBINE", payload)

    # endregion
