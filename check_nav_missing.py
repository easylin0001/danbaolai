import os
import re

docs_dir = '/Users/shensizaowu-designer/Documents/trae_projects/test_1/manual_docs'

target_nav = {
    '商品管理': [
        '商品管理',
        '商品添加',
        '商品采集',
        '商品分类',
        '商品规格',
        '商品评价',
        '商品品牌',
        '商品单位',
        '商品参数',
        '保障服务',
        '商品标签',
        '商品推荐',
    ],
    '用户管理': [
        '用户管理',
        '用户列表',
        '用户分组',
        '用户标签',
        '用户设置',
        '用户等级',
        '新人礼包',
        '激活有礼',
        '优惠券',
        '活动说明',
        '优惠券活动',
        '账号注销',
    ],
    '订单管理': [
        '订单管理',
        '订单发货',
        '订单退款',
        '订单打印',
        '订单提醒',
    ],
    '客服管理': [
        '客服管理',
        '客服功能',
        '客服接待',
    ],
    '营销管理': [
        '营销管理',
        '抽奖',
        '活动说明',
        '抽奖活动',
        '礼品卡',
        '功能说明',
        '拼团',
        '拼团活动',
        '秒杀',
        '秒杀活动',
        '砍价',
        '砍价活动',
        '积分',
        '积分商城',
        '积分介绍',
        '积分配置',
        '每日签到',
        '签到活动',
        '付费会员',
        '优惠套餐',
        '余额充值',
        '优惠活动',
        '限时折扣',
        '满减满折',
        '满送活动',
        '第N件N折',
        '活动规则',
        '活动背景图',
        '活动边框',
        '好友送礼',
        '收送礼品',
        '自动化运营',
        '智能推送',
        '生日有礼',
    ],
    '内容管理': [
        '内容管理',
        '社区',
        '社区话题',
        '社区内容',
        '社区评论',
        '社区设置',
        '文章',
        '文章管理',
        '文章分类',
    ],
    '直播管理': [
        '直播管理',
        '阿里云直播配置',
        '阿里云资费说明',
        'OBS',
        '直播列表',
        '中控台',
        '观众列表',
        '直播统计',
        '直播设置',
        '小程序直播',
        '直播间管理',
        '直播商品管理',
        '主播管理',
    ],
    '分销管理': [
        '分销管理',
        '分销员申请',
        '分销介绍',
        '分销配置',
        '分销等级',
        '分销员管理',
        '佣金提现',
        '团队管理',
        '团队列表',
        '代理商列表',
        '代理商申请',
        '团队配置',
        '团队统计',
        '团队订单',
        '返佣说明',
    ],
    '财务管理': [
        '财务管理',
        '财务操作',
        '财务记录',
        '佣金记录',
    ],
    '商城装修': [
        '商城装修',
        '主页装修',
        '商品详情',
        '个人中心',
        '商品分类',
        '页面配置',
        '主题风格',
        'PC页面',
        '系统表单',
        '悬浮按钮',
    ],
    '移动端商家管理': [
        '移动端商家管理',
        '商家管理开关',
        '工作台模块',
        '商品管理',
        '订单管理',
        '扫码核销',
        '售后维权',
        '用户管理',
        '代客下单',
    ],
    '商城设置': [
        '商城设置',
        '系统设置',
        '同城配送',
        '商品设置',
        '商城邮费',
        '邮费结构',
        '发货设置',
        '运费模板',
        '物流公司',
        '城市数据',
        '配送员管理',
        '支付设置',
        '交易设置',
        '定时任务',
        '政策协议',
        '单据设置',
    ],
    '应用设置': [
        '应用设置',
        '服务号',
        '小程序',
        'PC',
        'APP',
    ],
    '第三方接口': [
        '第三方接口',
        '一号通配置',
        '小票打印配置',
        '采集商品配置',
        '物流查询',
        '电子面单',
        '地图配置',
        '短信',
    ],
    '企业微信': [
        '企业微信',
        '客户管理',
        '企业渠道码',
        '欢迎语',
        '员工列表',
        '客户列表',
        '客户群发',
        '朋友圈列表',
        '客户群运营',
        '客户群列表',
        '自动拉群',
        '客户群群发',
        '企业微信设置',
    ],
    '供应商': [
        '供应商',
        '供应商申请',
        '供应商管理',
        '供应商财务',
        '供应商菜单设置',
        '供应商后台',
        '供应商商品',
        '供应商订单',
        '财务信息',
        '供应商设置',
        '供应商硬件配置',
    ],
    '采购商': [
        '采购商',
        '采购商说明',
    ],
    '商城硬件': [
        '商城硬件',
    ],
    '移动端UI鉴赏': [
        '移动端UI鉴赏',
    ],
    '商城AI': [
        '商城AI',
        '功能介绍',
    ],
    '库存管理': [
        '库存管理',
        '入库管理',
        '出库管理',
        '库存查询',
        '库存盘点',
        '出入库记录',
    ],
}

existing_pages = {}
for filename in os.listdir(docs_dir):
    if filename.startswith('page_') and filename.endswith('.html'):
        filepath = os.path.join(docs_dir, filename)
        page_id = filename.replace('page_', '').replace('.html', '')
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read(5000)
            title_match = re.search(r'<title>([^<]+)</title>', content)
            if title_match:
                title = title_match.group(1)
                title = title.replace('会员电商系统', '').replace(' - DANBAOLAI文档', '').strip()
                existing_pages[page_id] = title

output = []
output.append("=" * 70)
output.append("现有页面统计")
output.append("=" * 70)
output.append(f"总页面数: {len(existing_pages)}")

output.append("\n" + "=" * 70)
output.append("目标导航需要的页面检查")
output.append("=" * 70)

all_needed = []
for section, items in target_nav.items():
    for item_name in items:
        all_needed.append((section, item_name))

output.append(f"\n需要的页面总数: {len(all_needed)}")

output.append("\n" + "=" * 70)
output.append("逐项检查结果:")
output.append("=" * 70)

found_items = {}
missing_items = []

for section, item_name in all_needed:
    found = False
    found_id = None
    found_title = None
    
    for page_id, title in existing_pages.items():
        if item_name == title:
            found = True
            found_id = page_id
            found_title = title
            break
    
    if found:
        found_items[item_name] = (found_id, found_title)
        output.append(f"✓ [{section}] {item_name} -> page_{found_id}.html")
    else:
        missing_items.append((section, item_name))
        output.append(f"✗ [{section}] {item_name} -> 缺失!")

output.append("\n" + "=" * 70)
output.append(f"统计: 找到 {len(found_items)} 个, 缺失 {len(missing_items)} 个")
output.append("=" * 70)

if missing_items:
    output.append("\n缺失的页面列表:")
    for section, item in missing_items:
        output.append(f"  - [{section}] {item}")

result = '\n'.join(output)
print(result)

with open('/Users/shensizaowu-designer/Documents/trae_projects/test_1/nav_check_result.txt', 'w', encoding='utf-8') as f:
    f.write(result)
