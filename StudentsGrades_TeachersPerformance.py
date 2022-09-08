#coding=utf8
from STClasses import Students,Teachers
import random as rm
import pandas as pd
import matplotlib.pyplot as plt
import os

def createName(n):
    '''
    生成名字，n为生成个数
    '''
    names = []
    lastName = ["赵","钱","孙","李","周","吴","郑","王","冯","陈","褚","卫","蒋","沈","韩","杨","朱","秦","尤","许","何","吕","施","张","孔","曹","严","华","金","魏","陶","姜","戚","谢","邹","喻","柏","水","窦","章","云","苏","潘","葛","奚","范","彭","郎","鲁","韦","昌","马","苗","凤","花","方","俞","任","袁","柳","酆","鲍","史","唐","费","廉","岑","薛","雷","贺","倪","汤","滕","殷","罗","毕","郝","邬","安","常","乐","于","时","傅","皮","卞","齐","康","伍","余","元","卜","顾","孟","平","黄","和","穆","萧","尹","姚","邵","湛","汪","祁","毛","禹","狄","米","贝","明","臧","计","伏","成","戴","谈","宋","茅","庞","熊","纪","舒","屈","项","祝","董","梁","杜","阮","蓝","闵","席","季","麻","强","贾","路","娄","危","江","童","颜","郭","梅","盛","林","刁","钟","徐","邱","骆","高","夏","蔡","田","樊","胡","凌","霍","虞","万","支","柯","昝","管","卢","莫","经","房","裘","缪","干","解","应","宗","丁","宣","贲","邓","郁","单","杭","洪","包","诸","左","石","崔","吉","钮","龚","程","嵇","邢","滑","裴","陆","荣","翁","荀","羊","于","惠","甄","曲","家","封","芮","羿","储","靳","汲","邴","糜","松","井","段","富","巫","乌","焦","巴","弓","牧","隗","山","谷","车","侯","宓","蓬","全","郗","班","仰","秋","仲","伊","宫","宁","仇","栾","暴","甘","钭","厉","戎","祖","武","符","刘","景","詹","束","龙","叶","幸","司","韶","郜","黎","蓟","溥","印","宿","白","怀","蒲","邰","从","鄂","索","咸","籍","赖","卓","蔺","屠","蒙","池","乔","阴","郁","胥","能","苍","双","闻","莘","党","翟","谭","贡","劳","逄","姬","申","扶","堵","冉","宰","郦","雍","却","璩","桑","桂","濮","牛","寿","通","边","扈","燕","冀","浦","尚","农","温","别","庄","晏","柴","瞿","阎","充","慕","连","茹","习","宦","艾","鱼","容","向","古","易","慎","戈","廖","庾","终","暨","居","衡","步","都","耿","满","弘","匡","国","文","寇","广","禄","阙","东","欧","殳","沃","利","蔚","越","夔","隆","师","巩","厍","聂","晁","勾","敖","融","冷","訾","辛","阚","那","简","饶","空","曾","毋","沙","乜","养","鞠","须","丰","巢","关","蒯","相","查","后","荆","红","游","郏","竺","权","逯","盖","益","桓","公","仉","督","岳","帅","缑","亢","况","郈","有","琴","归","海","晋","楚","闫","法","汝","鄢","涂","钦","商","牟","佘","佴","伯","赏","墨","哈","谯","篁","年","爱","阳","佟","言","福","南","火","铁","迟","漆","官","冼","真","展","繁","檀","祭","密","敬","揭","舜","楼","疏","冒","浑","挚","胶","随","高","皋","原","种","练","弥","仓","眭","蹇","覃","阿","门","恽","来","綦","召","仪","风","介","巨","木","京","狐","郇","虎","枚","抗","达","杞","苌","折","麦","庆","过","竹","端","鲜","皇","亓","老","是","秘","畅","邝","还","宾","闾","辜","纵","侴","万俟","司马","上官","欧阳","夏侯","诸葛","闻人","东方","赫连","皇甫","羊舌","尉迟","公羊","澹台","公冶","宗正","濮阳","淳于","单于","太叔","申屠","公孙","仲孙","轩辕","令狐","钟离","宇文","长孙","慕容","鲜于","闾丘","司徒","司空","兀官","司寇","南门","呼延","子车","颛孙","端木","巫马","公西","漆雕","车正","壤驷","公良","拓跋","夹谷","宰父","谷梁","段干","百里","东郭","微生","梁丘","左丘","东门","西门","南宫","第五","公仪","公乘","太史","仲长","叔孙","屈突","尔朱","东乡","相里","胡母","司城","张廖","雍门","毋丘","贺兰","綦毋","屋庐","独孤","南郭","北宫","王孙"]
    firstName = ["贵财","军业","安会","秋鸿","先敏","小琼","天祥","林秀","成芳","钰莲","香盛","学碧","华兰","长英","春华","一路","文秀","小萍","燕琼","泽东","华常","才东","礼建","显斌","秀英","永玲","伟清","隆树","燕萍","茗民","仕芬","金国","春燕","智砝","学蓉","翠华","启菊","运斌","开芳","中华","清贵","小均","武民","艳琼","路容","礼琼","金木","华琼","金花","建均","明珍","晓梅","竹维","俊如","玉芳","春梅","永红","碧惠","兴碧","忠元","建菊","安杰","兴会","洪全","丽君","德贵","昌浩","春玲","荣琼","光贵","德飞","正艳","德发","春莲","英均","廷财","芝荣","仲琼","乐贵","宗和","礼艳","茂清","国辉","忠林","国会","通菊","达乡","邦菊","晓平","开兰","其海","万青","光丽","德菊","金美","安发","东群","雪英","晓斌","素红","仲碧","碧秀","成忠","兴容","芝凤","君秀","元芬","秀兰","凌艳","清清","杨琼","艳芬","正和","琼芳","克兰","秀兰","映君","翠华","小春","永红","小丽","廷光","克蓉","俊先","明菊","惠碧","冬梅","晓蓉","兴波","本波","国芹","孝珍","怀蓉","宗秀","远珍","菊蓉","芳兰","治霖","兴琼","晓华","素蓉"]
    lastname = [lastName[i] for i in range(0, n)]
    firstname = [firstName[i] for i in range(0, n)]
    for i in range(0, n):
        name = lastname[i] + firstname[i]
        names.append(name)
    return names

def createID(n):
    '''
    生成ID号，n为生成个数
    randint(m,n)为随机生成范围
    '''
    IDs = []
    while True:
        if len(IDs) < n:
            temp = rm.randint(2021001, 2021060)
            while temp not in IDs:
                IDs.append(temp)
        else:
            break
    return IDs

def createManage(n):
    manage = []
    for i in range(0, n):
        temp = rm.randint(0,1)
        manage.append(temp)
    return manage

def assignInfo(stuNum, teaNum, stuTotalNames, stuTotalIDs, teaTotalNames, teaTotalIDs):
    '''
    peopleNames,peopleIDs = []
    for i in range(0, n):
        temp = "people" + i
        temp = Classname(names[i], IDs[i])
        pelpleNames.append(temp.name)
        peopleIDs.append(temp.ID)
    '''

    stuNames = []
    stuIDs = []
    teaNames = []
    teaIDs = []
    for i in range(0, stuNum):
        tempStu = Students(stuTotalNames[i], stuTotalIDs[i])
        stuNames.append(tempStu.name)
        stuIDs.append(tempStu.ID)
    for i in range(0, teaNum):
        tempTea = Teachers(teaTotalNames[i], teaTotalIDs[i])
        teaNames.append(tempTea.name)
        teaIDs.append(tempTea.JN)

    return stuNames,stuIDs,teaNames,teaIDs



def write_into_excel(path, stuSheetName, teaSheetName, stuNames, stuIDs, teaNames, teaIDs, teaManage):
    writer = pd.ExcelWriter(path)
    stuInfo = pd.DataFrame({"ID": stuIDs, "Name": stuNames}, columns=['ID', 'Name'])
    teaInfo = pd.DataFrame({"ID": teaIDs, "Name": teaNames, \
                            "Displine":["语文", "数学", "英语", "地理", "历史", "政治", "体育", "音乐", "画画", "物理", "化学",],  \
                           "Manage": teaManage},
                           columns=['ID', 'Name', 'Displine', 'Manage'])
    stuInfo.to_excel(excel_writer = writer, sheet_name = stuSheetName)
    teaInfo.to_excel(excel_writer = writer, sheet_name = teaSheetName)
    writer.save()
    writer.close()
    return

def createGrades(Chinese, Math, English, Geography, History, Politics, PE, Music, FineArt, Physics, Chemistry):
    subjects = [Chinese, Math, English, Geography, History, Politics, PE, Music, FineArt, Physics, Chemistry]
    Chi=[]
    Ma=[]
    Eng=[]
    Geo=[]
    His=[]
    Pol=[]
    P=[]
    Mus=[]
    FA=[]
    Phy=[]
    Che=[]
    subjectslist = [Chi, Ma, Eng, Geo, His, Pol, P, Mus, FA, Phy, Che]
    for i in subjects:
        pos = subjects.index(i)
        for j in range(0, i):
            tempGrade = rm.randint(90, 100)
            subjectslist[pos].append(tempGrade)
        for k in range(0, 60-i):
            tempGrade = rm.randint(0, 89)
            subjectslist[pos].append(tempGrade)
    return Chi, Ma, Eng, Geo, His, Pol, P, Mus, FA, Phy, Che

def write_grades_into_excel(path, stuSheetName, teaSheetName, Chinese, Math, English, Geography, History, Politics, PE, Music, FineArt):
    writer = pd.ExcelWriter(path)
    subjects = [Chinese, Math, English, Geography, History, Politics, PE, Music, FineArt]
    subjectslist = ["语文", "数学", "英语", "地理", "历史", "政治", "体育", "音乐", "画画"]
    grades = pd.DataFrame(pd.read_excel(path, sheet_name = stuSheetName))
    teaInfo = pd.DataFrame(pd.read_excel(path, sheet_name= teaSheetName))
    for i in range(3, 12):
        grades.insert(i, subjectslist[i-3], subjects[i-3])
    grades.to_excel(excel_writer=writer, sheet_name = stuSheetName, index=False)
    teaInfo.to_excel(excel_writer=writer, sheet_name = teaSheetName, index=False)
    writer.save()
    writer.close()
    return

def changeGrades(path, teaSheetName, stuSheetName, stuNum, exam):
    writer = pd.ExcelWriter(path)
    teaInfo = pd.DataFrame(pd.read_excel(path, sheet_name=teaSheetName))
    stuInfo = pd.DataFrame(pd.read_excel(path, sheet_name=stuSheetName))
    for i in range(0, 9):
        subjects = ["语文", "数学", "英语", "地理", "历史", "政治", "体育", "音乐", "画画"]
        if int(exam) == 0:
            subjectslist = ["语文（期末）", "数学（期末）", "英语（期末）", "地理（期末）", "历史（期末）", "政治（期末）", "体育（期末）", "音乐（期末）", "画画（期末）"]
        elif int(exam) == 1:
            subjectslist = ["语文（月考）", "数学（月考）", "英语（月考）", "地理（月考）", "历史（月考）", "政治（月考）", "体育（月考）", "音乐（月考）", "画画（月考）"]
        elif int(exam) == 2:
            subjectslist = ["语文（中考）", "数学（中考）", "英语（中考）", "地理（中考）", "历史（中考）", "政治（中考）", "体育（中考）", "音乐（中考）", "画画（中考）"]
        curcolsnum = stuInfo.shape[1]
        stuInfo.insert(curcolsnum, subjectslist[i], None)
        if teaInfo.loc[i, 'Manage'] == 0:
            stuInfo.sort_values(by=subjects[i], ascending=False)
            rise = int(stuNum*rm.uniform(0, 0.03))
            decline = int(stuNum*0.05)
            totalchange = int(rise + decline) + 1
            declinenum = 0
            risenum = 0
            for j in range(0, totalchange):
                temp = rm.randint(0, 59)
                if declinenum < decline:
                    stuInfo.loc[temp, subjectslist[i]] = int(stuInfo.loc[temp, subjects[i]]) - rm.randint(1,10) if int(stuInfo.loc[temp, subjects[i]]) > 10 else int(stuInfo.loc[temp, subjects[i]]) - 1
                    declinenum += 1
                elif risenum < rise:
                    stuInfo.loc[temp, subjectslist[i]] = int(stuInfo.loc[temp, subjects[i]]) + rm.randint(1,10) if int(stuInfo.loc[temp, subjects[i]]) < 90 else int(stuInfo.loc[temp, subjects[i]]) + 1
                    risenum += 1
                else:
                    stuInfo.loc[stuInfo[subjectslist[i]].isnull(), subjectslist[i]] = stuInfo[subjects[i]]
        else:
            stuInfo.sort_values(by=subjects[i], ascending=False)
            decline = int(stuNum * rm.uniform(0, 0.03))
            rise = int(stuNum * 0.05)
            totalchange = int(rise + decline) + 1
            declinenum = 0
            risenum = 0
            for j in range(0, totalchange):
                temp = rm.randint(0, 59)
                if declinenum < decline:
                    stuInfo.loc[temp, subjectslist[i]] = int(stuInfo.loc[temp, subjects[i]]) - rm.randint(1, 10) if int(stuInfo.loc[temp, subjects[i]]) > 10 else int(stuInfo.loc[temp, subjects[i]]) - 1
                    declinenum += 1
                elif risenum < rise:
                    stuInfo.loc[temp, subjectslist[i]] = int(stuInfo.loc[temp, subjects[i]]) + rm.randint(1, 10) if int(stuInfo.loc[temp, subjects[i]]) < 90 else int(stuInfo.loc[temp, subjects[i]]) + 1
                    risenum += 1
                else:
                    stuInfo.loc[stuInfo[subjectslist[i]].isnull(), subjectslist[i]] = stuInfo[subjects[i]]
    stuInfo.to_excel(excel_writer = writer, sheet_name = stuSheetName, index = False)
    teaInfo.to_excel(excel_writer = writer, sheet_name = teaSheetName, index = False)
    writer.save()
    writer.close()

def countBonus(path, stuSheetName, teaSheetName):
    writer = pd.ExcelWriter(path)
    stuInfo = pd.DataFrame(pd.read_excel(path, sheet_name = stuSheetName))
    teaInfo = pd.DataFrame(pd.read_excel(path, sheet_name = teaSheetName))
    subjects = ["语文", "数学", "英语", "地理", "历史", "政治", "体育", "音乐", "画画"]
    subjectslist = ["Chinese", "Math", "English", "Geography", "History", "Politics", "PE", "Music", "FineArt"]
    exams = ["", "（期末）", "（月考）", "（中考）"]
    curcolsnum = teaInfo.shape[1]
    teaBonusCount = []
    for i in range(0, 9):
        count = 0
        for j in exams:
            subject_exam = subjects[i] + j
            for n in range(0, 60):
                if i <= 2:
                    if stuInfo[subject_exam][n] >= 90:
                        count += 1
                    elif stuInfo[subject_exam][n] >= 80:
                        count += 0.3
                    elif stuInfo[subject_exam][n] < 60:
                        count -= 0.1
                else:
                    if stuInfo[subject_exam][n] >= 90:
                        count += 0.3
                    elif stuInfo[subject_exam][n] >= 80:
                        count += 0.1
                    elif stuInfo[subject_exam][n] < 60:
                        count -= 0.1
            count = round(count, 1)
        teaBonusCount.append(count)
    for i in range(0, 2):
        teaBonusCount.append(0)
    teaInfo.insert(curcolsnum, "绩效", teaBonusCount)
    stuInfo.to_excel(excel_writer = writer, sheet_name = stuSheetName, index = False)
    teaInfo.to_excel(excel_writer = writer, sheet_name = teaSheetName, index = False)
    writer.save()
    writer.close()
    teaBonus = dict(zip(subjectslist, teaBonusCount))
    return teaBonus

def statisticalChart(Bonus):
    BonusTuple = sorted(Bonus.items(), key = lambda i:(i[1], i[0]), reverse = True)
    teacher = []
    teaBonus = []
    for i in range(0, 5):
        teacher.append(BonusTuple[i][0])
        teaBonus.append(BonusTuple[i][1])
    fig,ax = plt.subplots(2, 1, figsize = (12, 8), sharex = "col")
    ax[0].bar(teacher, teaBonus)
    ax[1].plot(teacher, teaBonus)
    plt.show()

#path为文件路径（包括excel文件名+后缀），StuInfo为excel文件中的成绩表（Sheet1），TeaInfo为excel文件中的老师信息表（Sheet2）
if __name__=="__main__":
    stuTotalNames = createName(60)
    stuTotalIDs = createID(60)
    teaTotalNames = createName(11)
    teaTotalIDs = createID(11)
    teaManage = createManage(11)
    stuNames,stuIDs,teaNames,teaIDs = assignInfo(60, 11, stuTotalNames, stuTotalIDs, teaTotalNames, teaTotalIDs)
    path = os.getcwd() + "\\SchoolTest.xlsx"
    stuSheetName = "StuInfo"
    teaSheetName = "TeaInfo"
    write_into_excel(path, stuSheetName, teaSheetName, stuNames, stuIDs, teaNames, teaIDs, teaManage)

    Chinese, Math, English, Geography, History, Politics, PE, Music, FineArt, Physics, Chemistry = \
        createGrades(12, 18, 20, 10, 45, 30, 50, 58, 52, 23, 24)
    write_grades_into_excel(path, stuSheetName, teaSheetName, Chinese, Math, English, Geography, \
                            History, Politics, PE, Music, FineArt)
    for i in range(0, 3):
        changeGrades(path, teaSheetName, stuSheetName, 60, i)
    Bonus = countBonus(path, stuSheetName, teaSheetName)
    statisticalChart(Bonus)