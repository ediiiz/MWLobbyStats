import json
import pandas as pd
import requests
from nested_lookup import get_occurrence_of_key

usernames = []
kd_ratios = []
accuracys = []
platform = []
score_per_minute = []
usernames_check = []
usernames_check_atv_id = []
usernames_check_atv_id_2 = []
usernames_check_psn = []
usernames_check_xbl = []
break_loop = []
cookie_data = []
fromapi_usernames = []
working_cookie = ""


# cookie_data.append("XSRF-TOKEN=EgTXmLiFIWum1VzOnzAZIqftNRBGzV9VLNGswptKL99wywVrmDX2AnYlDYhU5a_I; new_SiteId=cod; comid=cod; ACT_SSO_COOKIE=MTA0NzQ2NzAyNzgwNjExMTI5NjI6MTU5MDM3MzY4NzU4ODo4MWZjZjBjZTAyMGNlNDc0ZGQzNTc4OTVlMjE2N2MzNw; s_ACT_SSO_COOKIE=MTA0NzQ2NzAyNzgwNjExMTI5NjI6MTU5MDM3MzY4NzU4ODo4MWZjZjBjZTAyMGNlNDc0ZGQzNTc4OTVlMjE2N2MzNw; atkn=eyJhbGciOiAiQTEyOEtXIiwgImVuYyI6ICJBMTI4R0NNIiwgImtpZCI6ICJ1bm9fcHJvZF9sYXNfMSJ9.bUatf2d3TLWEejO0oEeqS_sqvxtjPDPHiT9iv-WyrEVHraO9m0Hbkw.St31xMBV6i34iXfa.6BCh5yOlByPPWwZZ73-w8XgImcVL0ujw_IlQXhJt7J-99R2NeRvczgFa5XdvisZCdiJ8taD0UyTQotI6c5teAZgdMsrR8vqpEIzC4-sfhylJpSXPcCFDHNKG8toBoYe0Lb3mfj2F1Hzslv_P-3Dnf6i31N6PvaDXLvee1dpaT9MnCw9sfCIjPiVdb5FnIGKgI-56_IxsXk6G-9lA__1GiOyZC3DpSic6gOawatY5n56BG0kDnO5VmJdMqzGgZVAHj2qLcfmJfX0Aoqe19QnfB4jv4e9HtTSz1FZSVw7yi-0Pv2uhXyShLlOqtsXoyM73skiryqTojISZZi1gID7KUiWY4lLO9Mb9PDVgFOaH6hlEIV_0JpW6gpM27rnGqpJhRZY_WCfK249guU5glqtKF1GVV-vSFhucppSv4IIpQ1Fp-o9IBz6bB79z-XpsCN1Fep2xkQSdimU.6O80wfrektz6DsXg08nw3g; rtkn=eyJhbGciOiAiQTEyOEtXIiwgImVuYyI6ICJBMTI4R0NNIiwgImtpZCI6ICJ1bm9fcHJvZF9sYXNfMSJ9.HM9dHddvO37_ObZssATeAfuupuRQywuzubDlBh-P95D50joSYG_6TQ.yOoCULc82pIqC1kv.Mcqu7Vz7TcruKcvwQtJXw7d_SJa0kooE7J6sM4ICb3KYMA55mE_CQyy2f7LAHJtEQbIO--iRhzXaGMHmCems6I-Db7ErQ2xjBNiyMRp7RR15Hq0481SDY0sPFss0q-lLjSiAJDhJH7Sv9V1RfWw39F89hqLfeY393-jYq7fTIV7o-OiwNFF3HdmAaiQxHVachv_1bIpPYTcukEThgHxiacIwc0ySjIwHbITScyZN0e5u3PFGey3DKjX26hOFPXIFbqsXwxlyiOl705RvuWeJqX5TqUjXv57Hz_VMQ_chcBg80le63ZdmS4uqByZtVgTQr3_WfSF6GlgufzEH-fr_zK3Xv35ohNOOX5n2BQ8Ob9nc9ztJ5RlGbUO7DodP-qoAtLdz4tAqgvz82OZX26c8B-gZ3Og9OknL4IfTd-h-JJrp8t35dc5ja82LY9_TXbtCVOT3xqM_gcGGLwvVIOMNuWd1MAUWErGg1EoVqju67nEdT4ZvI9uCoiV9LhTfRvKQczpe2ZeF.KubDa3yrOW-d0a4ZPjCS6Q")
# cookie_data.append("XSRF-TOKEN=EgTXmLiFIWum1VzOnzAZIqftNRBGzV9VLNGswptKL99wywVrmDX2AnYlDYhU5a_I; new_SiteId=cod; comid=cod; ACT_SSO_COOKIE=OTM0MDgxNzU5MjMwODc2NTY1MzoxNTkwNTIwMDcyNTAzOmJjOWMzY2RhM2Q5YjgyNzM3NjcwMjhhYWY5NjgwYTNj; s_ACT_SSO_COOKIE=OTM0MDgxNzU5MjMwODc2NTY1MzoxNTkwNTIwMDcyNTAzOmJjOWMzY2RhM2Q5YjgyNzM3NjcwMjhhYWY5NjgwYTNj; atkn=eyJhbGciOiAiQTEyOEtXIiwgImVuYyI6ICJBMTI4R0NNIiwgImtpZCI6ICJ1bm9fcHJvZF9sYXNfMSJ9.ScbfX2mPYFt5EooY3RWs02K_33uRymm8rTdUfCy8IQskug5x6mCV7A.3hwfUao0JONkpObM.tuHThZSPxKmYX8hqwPn9-1AtO-HSH7apoZiLc5vDd4uAxkDQiqBstlI3Qdjr3OOax0ziPrEfBayqVGn5KhyJ9-MmBgmr5RNbGuYIzm5wbA0K2fFp5PWqlOX-HEdOD7IjDVj9aDE1YyLFBExXNKS2xiFYPACHJ-wiJCm1B3ju5uij-deqtb6YFTVLBLc6l1chYeKji_crs1wWfNrddqxWg1XB2aKoM-xZVuhhJG_jKopWaUEFprF4pBU9Mm1w1X_k9vKeG1eQYurz8QILOFhTL827-Fr6Gs_TvNIlHzv_OurlDSQEzX7WXp6hLJ8Mkr4Mw5kzZSqrrGMaLtLNhlasUlwXfy9kbmAXKLXYYrizhtl2eaELw1wBEF5M6bNFFoYdycvnYMy_nanpt46qQCmSLpJB3dcMdA-SsX5sAOyDn1LGbcZwuIqFVNsXRodbnJDd2fmiFwgl.83GwhbUH0XZeEM0SK_HuPg; rtkn=eyJhbGciOiAiQTEyOEtXIiwgImVuYyI6ICJBMTI4R0NNIiwgImtpZCI6ICJ1bm9fcHJvZF9sYXNfMSJ9.na_KxrjfRfPfykkuxL9FIZLvv4xV0cIYvTfmV2HAvGRkh63Jj1zyNg.nc0_p9ZDnEyzaB7N.y7LOmLBAgXpu4ULT3erOAFQuRpS3oUb1_HG7Xf5n2cQACBrPK9ftIvleSlCuGkgt0RcgLnqdo2WR_2Bbp8-jaw7k8JwQK4h55GLbrKrIUrhTnuDInXq8qzCbo2VK9Mf92NRhj9Ahq5Csp8P0JlQzOoq7d5qK29x3Jpwd3kgN9Xk4yvnVEaCwqbBpAdb6_GfLZfBQETvR4Pn7_P6We31rs4aGeS3e5HCnY7SOawDU6ugfaqi7RTNE3qYYWaFK-61OsHr4lqtAl0g6AWsXsiRAxaNOLLWGGd4ouiezyAON3MgNmF6O2ZD9UDgiTw7BxyBUcN0e-9n5icsHTyaaD_IjLgdLhtjD2FCMiRrnCCwrglxFqGzME1ssFg_54wsm-BOhZViu7bUrHxd6HeyH2XICIuiedD31xmnTlkaVpT5pLa43i_zy0OhTLXOcdZO7pAqt7P6HXCsIGz_esxtYABt7miXYubQMAdJw87gv94VG95JD0LUmOzVb_wbv_H2ebd2h9TVRog.8emGkMX1-QJqD9ySnjTDFg")


def check_api_call_cookie():
    global working_cookie
    for x in range(0, cookie_data.__len__()):
        print("Checking Cookie: " + str(x + 1))
        r = requests.get(
            "https://www.callofduty.com/api/papi-client/crm/cod/v2/platform/uno/username/" + str(x) + "/search",
            headers={"Cache-Control": "private", "Cookie": "" + cookie_data[x]})
        json_username_data = json.loads(r.content)

        # data = dump.dump_all(r)
        # print(data.decode('utf-8'))

        if json_username_data["status"] == "error":
            return False
            # time.sleep(5)
        else:
            print("Cookie works")
            working_cookie = cookie_data[x]
            break


def request(platform, username_links):
    r = requests.get(
        "https://www.callofduty.com/api/papi-client/crm/cod/v2/platform/" + platform + "/username/" + username_links + "/search",
        headers={"Cookie": "" + working_cookie})
    json_username_data = json.loads(r.content)
    # print(r.content)
    # print(json_username_data)
    # print(json.dumps(json_username_data, indent=4))
    # keytotal = (get_occurrence_of_key(json_username_data, "username"))
    # print(keytotal)
    if json_username_data["status"] == "Error":
        break_loop.append("1")
    else:
        return json_username_data


def getUsernames(username_links):
    try:
        if username_links == "vvvvNextgame":
            print("next Game")
            tablelength = usernames.__len__()
            print(tablelength)
            usernames.append("Next Game")
            platform.append("Next")
            kd_ratios.append("NA")
            accuracys.append("NA")
            score_per_minute.append("NA")

        if username_links not in usernames_check_atv_id_2:
            print("request ATV")
            json_username_data = request("uno", username_links)
            keytotal_atv_id = (get_occurrence_of_key(json_username_data, "username"))
            # print(keytotal)
            usernames_check_atv_id_2.append(username_links)
            for x in range(0, keytotal_atv_id):
                fromapi_usernames.append(json_username_data["data"][x]["username"])
        if json_username_data["data"] == []:
            try:
                print("request PSN")
                # print("player not in DB: ATV ID")
                usernames_check_atv_id.append(username_links)
                json_username_data = request("psn", username_links)
                keytotal_psn = (get_occurrence_of_key(json_username_data, "username"))
                if keytotal_psn == 0:
                    try:
                        print("request XBL")
                        # print("player not in DB: psn")
                        usernames_check_psn.append(username_links)
                        json_username_data = request("xbl", username_links)
                        keytotal_xbl = (get_occurrence_of_key(json_username_data, "username"))
                        if keytotal_xbl == 0:
                            # print("player not in DB: xbl")
                            usernames_check_xbl.append(username_links)
                        for x in range(0, keytotal_xbl):
                            fromapi_usernames.append(json_username_data["data"][x]["username"])
                    except:
                        ("")
                for x in range(0, keytotal_psn):
                    fromapi_usernames.append(json_username_data["data"][x]["username"])
            except:
                ("")
    except:
        ""

    for x in range(fromapi_usernames.__len__()):
        if fromapi_usernames[x] not in usernames_check:
            getStats(fromapi_usernames[x])
            usernames_check.append(fromapi_usernames[x])
        else:
            continue


def getStats(username_stats):
    try:
        if username_stats not in usernames_check_atv_id:
            username_stats = username_stats.replace("#", "%23")
            r = requests.get(
                "https://www.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/uno/gamer/" + username_stats + "/profile/type/mp?locale=de",
                headers={"Cookie": "" + working_cookie})
            print(r.url)
            print("YES ATV")
            json_stats_data = json.loads(r.content)
            writeToList(username_stats, json_stats_data)
            # return (json.dumps(json_stats_data, indent=4))
        elif username_stats not in usernames_check_psn:
            # print(username_stats + " is not on ATV ID")
            username_stats = username_stats.replace("#", "%23")
            r = requests.get(
                "https://www.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/psn/gamer/" + username_stats + "/profile/type/mp?locale=de",
                headers={"Cookie": "" + working_cookie})
            print(r.url)
            print("YES PSN")
            json_stats_data = json.loads(r.content)
            writeToList(username_stats, json_stats_data)
        elif username_stats not in usernames_check_xbl:
            # print(username_stats + " is not on ATV ID")
            # (username_stats + " is not on PSN")
            username_stats = username_stats.replace("#", "%23")
            r = requests.get(
                "https://www.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/xbl/gamer/" + username_stats + "/profile/type/mp?locale=de",
                headers={"Cookie": "" + working_cookie})
            print(r.url)
            print("YES XBL")
            json_stats_data = json.loads(r.content)
            writeToList(username_stats, json_stats_data)
    except:
        usernames.remove(username_stats)
        print(username_stats + " has no Stats")


def writeToList(username_stats, json_stats_data):
    # print(username_stats)

    usernames.append(username_stats)
    if str(json_stats_data["data"]["platform"]).upper() != "NONE":
        platform.append(str(json_stats_data["data"]["platform"]).replace("uno", "ATV ID").upper())
    kd_ratios.append(str(json_stats_data["data"]["lifetime"]["all"]["properties"]["kdRatio"]).replace(".", ","))
    accuracys.append(str(json_stats_data["data"]["lifetime"]["all"]["properties"]["accuracy"]).replace(".", ","))
    score_per_minute.append(
        str(json_stats_data["data"]["lifetime"]["all"]["properties"]["scorePerMinute"]).replace(".", ","))


def listToCSV():
    df = pd.DataFrame(
        {'Name': usernames, "Platform": platform, 'KD': kd_ratios, 'Accuracy': accuracys, "SPM": score_per_minute})
    df.to_csv('Match.csv', index=False, encoding='utf-8')

# !DEBUGGING!
# print(check_api_call_cookie())
# getUsernames("vvvvNextgame")
# print(usernames)
# print(kd_ratios)
# print(accuracys)
# print(score_per_minute)
# print(platform)
# listToCSV()
