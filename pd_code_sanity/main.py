
# 检查 pd_code 的合法性
def sanity(pd_code:list[list[int | str]]) -> bool:
    cnt = dict()

    # 检查外层对象类型
    if not isinstance(pd_code, list):
        return False
    
    # 检查内层对象
    for crossing in pd_code:
        if not isinstance(crossing, list):
            return False
        
        # 检查元素个数合法
        if len(crossing) != 4:
            return False
        
        # 检查元素类型合法
        for term in crossing:

            # 检查内层对象类型
            if ((not isinstance(term, str)) 
                and (not isinstance(term, int))):
                return False
            
            # 统计每个对象出现次数
            if cnt.get(term) is None:
                cnt[term] = 0
            cnt[term] += 1 
    
    # 每个元素恰好出现两次
    for term in cnt:
        if cnt[term] != 2:
            return False

    return True
