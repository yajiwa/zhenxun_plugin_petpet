from .utils import Command
from .functions import *

commands = [
    Command(("万能表情", "空白表情"), universal),
    Command(("摸", "摸摸", "摸头", "摸摸头", "rua"), petpet),
    Command(("亲", "亲亲"), kiss),
    Command(("贴", "贴贴", "蹭", "蹭蹭"), rub),
    Command(("顶", "玩"), play),
    Command(("拍",), pat),
    Command(("撕",), rip),
    Command(("丢", "扔"), throw),
    Command(("抛", "掷"), throw_gif),
    Command(("爬",), crawl),
    Command(("精神支柱",), support),
    Command(("一直",), always),
    Command(("加载中",), loading),
    Command(("转",), turn),
    Command(("小天使",), littleangel),
    Command(("不要靠近",), dont_touch),
    Command(("一样",), alike),
    Command(("滚",), roll),
    Command(("玩游戏", "来玩游戏"), play_game),
    Command(("膜", "膜拜"), worship),
    Command(("吃",), eat),
    Command(("啃",), bite),
    Command(("出警",), police),
    Command(("警察",), police1),
    Command(("问问", "去问问"), ask),
    Command(("舔", "舔屏", "prpr"), prpr),
    Command(("搓",), twist),
    Command(("墙纸",), wallpaper),
    Command(("国旗",), china_flag),
    Command(("交个朋友",), make_friend),
    Command(("继续干活", "打工人"), back_to_work),
    Command(("完美", "完美的"), perfect),
    Command(("关注",), follow),
    Command(("我朋友说", "我有个朋友说"), my_friend),
    Command(("这像画吗",), paint),
    Command(("震惊",), shock),
    Command(("兑换券",), coupon),
    Command(("听音乐",), listen_music),
    Command(("典中典", "黑白草图"), dianzhongdian),
    Command(("哈哈镜",), funny_mirror),
    Command(("永远爱你",), love_you),
    Command(("对称",), symmetric),
    Command(("安全感",), safe_sense),
    Command(("永远喜欢", "我永远喜欢"), always_like),
    Command(("采访",), interview),
    Command(("打拳",), punch),
    Command(("群青",), cyan),
    Command(("捣",), pound),
    Command(("捶",), thump),
    Command(("需要", "你可能需要"), need),
    Command(("捂脸",), cover_face),
    Command(("敲",), knock),
    Command(("垃圾", "垃圾桶"), garbage),
    Command(("为什么@我", "为什么at我"), whyatme),
    Command(("像样的亲亲",), decent_kiss),
    Command(("啾啾",), jiujiu),
    Command(("吸", "嗦"), suck),
    Command(("锤",), hammer),
    Command(("紧贴", "紧紧贴着"), tightly),
    Command(("注意力涣散",), distracted),
    Command(("阿尼亚喜欢",), anyasuki),
    Command(("想什么",), thinkwhat),
    Command(("远离",), keepaway),
]