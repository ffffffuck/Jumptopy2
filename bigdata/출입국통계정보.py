import urllib.request
import datetime
import json
import math

access_key="PUjPcu22uUk09DaNdDl6mkVTDoMG2QJWGhxwAeQVqybmmJfBDw%2F2kb0ziRxy0smbezEH77TXCv%2BfCYGP7OkDfw%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)
    print(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success"%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s"%(datetime.datetime.now(),url))


#[CODE 1]
def getTourPointVisitor(yyyymm,natCd,edCd):

    end_point='http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

    parameters = "?_type=json&serviceKey="+access_key
    parameters += "&YM="+yyyymm
    parameters += "&NAT_CD=" +natCd
    parameters += '&ED_CD='+edCd

    url=end_point+parameters
    retData = get_request_url(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)

#[CODE 2]
#
# def getTourPointData(item,yyyymm,jsonResult):
#
#     natCd = 0 if 'natCd' not in item.keys() else item['natCd']
#     natKorNm = '' if 'natKorNm' not in item.keys() else item['natKorNm']
#     num = 0 if 'num'not in item.keys() else item['num']
#     edCd = '' if 'edCd' not in item.keys() else item['deCd']
#
#     jsonResult.append({'yyyymm':yyyymm,'natCd':natCd,'edCd':edCd,'num':num,'natKorNm':natKorNm})
#
#     return

def main():
    jsonResult = []

    national_code = '112'
    edCd = 'E'

    nStartYear = 2011
    nEndYear = 2017

    for year in range(nStartYear, nEndYear):
        for month in range(1,13):
            yyyymm = "{0}{1:0>2}".format(str(year),str(month))
            jsonData = getTourPointVisitor(yyyymm,national_code,edCd)

            if(jsonData['response']['header']['resultMsg']=='OK'):
                krName = jsonData['response']['body']['items']['item']['natKorNm']
                krName = krName.replace(' ','')
                iTotalVisit = jsonData['response']['body']['items']['item']["num"]
                print('%s_%s:%s'%(krName,yyyymm,iTotalVisit))

                jsonResult.append({'nat_name':krName,'nat_cd':national_code,'yyyymm':yyyymm,'visit_cnt':iTotalVisit})

    cnVisit = []
    VisitYM = []
    index = []

    i = 0

    for item in jsonResult:
        index.append(i)
        cnVisit.append(item['visit_cnt'])
        VisitYM.append(item['yyyymm'])

    with open('%s(%s)_해외방문객정보_%d_%d.json'%(krName,national_code,nStartYear,nEndYear-1),'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult,indent=4,sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)

if __name__ =='__main__':
    main()