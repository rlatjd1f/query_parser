import re

# alias_add_cols = ["CENTER_ID", "NODE_ID", "OSCOM_ID", "GRANT_ID", "ACCESS_SCOPE", "TENANT_ID", "IE_MENT_ID", "COMPANY_ID"]
alias_add_cols = []
col_dict = {}


def init():
    col_dict['GROUP'] = ["A", "COALESCE(GR{}.GROUP_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_IC_GROUPMASTER GR{} ON GR{}.FIRST_GROUP_ID = {}.{}"]
    col_dict['GRANT'] = ["A", "COALESCE(GM{}.GRANT_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_CC_GRANTMASTER GM{} ON GM{}.GRANT_ID = {}.{}"]
    col_dict['CENTER'] = ["A", "COALESCE(CM{}.GRANT_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_CC_CENTERMASTER CM{} ON CM{}.GRANT_ID = {}.{}"]
    col_dict['TENANT'] = ["A", "COALESCE(TT{}.TENANT_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_CC_TENANTMASTER TT{} ON TT{}.TENANT_ID = {}.{}"]
    col_dict['OSCOM'] = ["A", "COALESCE(OS{}.OSCOM_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_CC_OSCOMPANY OS{} ON OS{}.OSCOM_ID = {}.{}"]
    col_dict['COMPANY'] = ["A", "COALESCE(CT{}.COMPANY_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_CC_COMPANYMASTER CT{} ON CT{}.COMPANY_ID = {}.{}"]
    col_dict['ROUTE'] = ["A", "COALESCE(CT{}.ROUTE_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_IE_ROUTE RO{} ON RO{}.ROUTE_ID = {}.{}"]
    col_dict['CTIQ'] = ["A", "COALESCE(EA{}.MENT_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_IE_ANNOUNCEBGM AB{} ON AB{}.IE_MENT_ID = {}.{}"]
    col_dict['SYSTEM'] = ["A", "COALESCE(SM{}.SYSTEM_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_CC_SYSTEMMASTER SM{} ON SM{}.SYSTEM_ID = {}.{}"]
    col_dict['CDR_SYSTEM'] = ["A", "COALESCE(SM{}.SYSTEM_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_CC_SYSTEMMASTER SM{} ON SM{}.SYSTEM_ID = {}.{}"]
    col_dict['PROCESS'] = ["A", "COALESCE(CP{}.PROCESS_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_CC_SYSTEMPROCESS CP{} ON CP{}.SYSTEM_ID = {}.{}"]
    col_dict['NODE'] = ["A", "COALESCE(NM{}.NODE_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_CC_NODEMASTER NM{} ON NM{}.NODE_ID = {}.{}"]
    col_dict['DR_NODE'] = ["A", "COALESCE(NM{}.NODE_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_CC_NODEMASTER NM{} ON NM{}.NODE_ID = {}.{}"]
    col_dict['LICENSE'] = ["A", "COALESCE(LM{}.LICENSE_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_CC_LICENSEMASTER LM{} ON LM{}.LICENSE_ID = {}.{}"]
    col_dict['ANNOUNCEBGM'] = ["A", "COALESCE(AB{}.MENT_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_IE_ANNOUNCEBGM AB{} ON AB{}.IE_MENT_ID = {}.{}"]
    col_dict['PROGRAM'] = ["A", "COALESCE(PG{}.PROGRAM_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_CC_PROGRAM PG{} ON PG{}.PROGRAM_NO = {}.{}"]
    col_dict['ERRORCATEGORY'] = ["A", "COALESCE(EC{}.CATEGORY_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_CC_ERRORCATEGORY EC{} ON EC{}.CATEGORY_CD = {}.{}"]
    col_dict['USER'] = ["A", "COALESCE(UM{}.USER_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_CC_USERMASTER UM{} ON UM{}.USER_ID = {}.{}"]
    col_dict['SKILLSET'] = ["A", "COALESCE(CS{}.SKILLSET_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_IC_SKILLSET CS{} ON CS{}.SKILLSET_ID = {}.{}"]
    col_dict['DOD_TRANS'] = ["A", "COALESCE(DT{}.DOD_TRANS_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_IE_DOD_TRANSMASTER DT{} ON DT{}.DOD_TRANS_ID = {}.{}"]
    col_dict['DN_GROUP'] = ["A", "COALESCE(DG{}.DN_GRP_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_IE_DN_GROUPMASTER DG{} ON DG{}.DN_GROUP_ID = {}.{}"]
    col_dict['DEVICE_TYPE'] = ["A", "COALESCE(DI{}.DEVICE_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_IE_DN_DEVICEINFO DI{} ON DI{}.DEVICE_TYPE = {}.{}"]
    col_dict['WORKTIME'] = ["A", "COALESCE(WM{}.WORKTIME_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_IE_WORKTIME_MASTER WM{} ON WM{}.IE_WORKTIME_ID = {}.{}"]
    col_dict['SYS_CLASS'] = ["A", "COALESCE(SC{}.SYS_CLASS_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_CC_SYSTEMCLASS SC{} ON SC{}.SYS_CLASS_CD = {}.{}"]
    col_dict['ENDPOINT'] = ["A", "COALESCE(EP{}.ENDPT_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_IE_ENDPOINT EP{} ON EP{}.ENDPT_ID = {}.{}"]
    col_dict['SIP_TRUNK'] = ["A", "COALESCE(ST{}.SIP_TRUNK_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_IE_SIP_TRUNK ST{} ON ST{}.SIP_TRUNK_ID = {}.{}"]
    col_dict['SIP_TRUNK_NO'] = ["A", "COALESCE(ST{}.SIP_TRUNK_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_IE_SIP_TRUNK ST{} ON ST{}.SIP_TRUNK_ID = {}.{}"]
    col_dict['SERVICE'] = ["A", "COALESCE(SM{}.SERVICE_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_IR_SERVICEMASTER SM{} ON SM{}.SERVICE_ID = {}.{}"]
    col_dict['BRANCH_CODE'] = ["A", "COALESCE(BR{}.BRANCH_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_CC_BRANCH BR{} ON BR{}.BRANCH_CODE = {}.{}"]
    col_dict['AGENT'] = ["A", "COALESCE(AG{}.AGENT_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_IC_AGENTMASTER AG{} ON AG{}.AGENT_ID = {}.{}"]
    col_dict['QUEUE'] = ["A", "COALESCE(QM{}.CTIQ_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_IC_CTIQ_MASTER QM{} ON QM{}.CTIQ_ID = {}.{}"]
    col_dict['ACS'] = ["A", "COALESCE(ACS{}.ACS_SERVICE_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_IR_ACS_SERVICE_MASTER ACS{} ON ACS{}.ACS_ID = {}.{}"]
    col_dict['CAMPAIGN'] = ["A", "COALESCE(CM{}.CAMPAIGN_NAME,N'N/A') AS {}", "LEFT OUTER JOIN TB_IR_ACS_CAMPAIGN_MASTER CM{} ON CM{}.CAMPAIGN_ID = {}.{}"]

    # col_dict add from tb_common_code with file read
    with open("tb_common_code.txt", "r", encoding="UTF-8") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue

            col_keyword, val1, val2, val3 = line.split("|")
            col_dict[col_keyword] = [val1, val2, val3]


def main():
    init()
    col_list = col_dict.keys()
    ori_query_list = []
    new_query_list = []
    new_cond_list = []
    mst_table_alias = "A"
    from_line = 0
    where_line = 0

    with open("parsing.sql", "r", encoding="UTF-8") as file:
        try:
            for line in file:
                while "  " in line:
                    line = line.strip().replace("  ", " ")

                while "\t" in line:
                    line = line.strip().replace("\t", " ")

                ori_query_list.append(line.strip())
                print(line)
        except Exception as e:
            print(line)
            print("error msg: {}".format(e))

    print(";")
    print("")

    for idx, line in enumerate(ori_query_list):
        if line.split(" ")[0] == "FROM":
            last_col_line = new_query_list[len(new_query_list) - 1]
            if last_col_line[len(last_col_line) - 1] == ",":
                new_query_list[len(new_query_list) - 1] = last_col_line[:len(last_col_line) - 1]

            from_line = idx
            if len(line.split(" ")) == 3:
                mst_table_alias = line.split(" ")[2].strip()

        elif line.split(" ")[0] == "WHERE":
            where_line = idx

            tmp_list = line.split(" ")
            for idx2, tmp_str in enumerate(tmp_list):
                if tmp_str in alias_add_cols and "." not in tmp_str:
                    tmp_list[idx2] = "{}.{}".format(mst_table_alias, tmp_str)
            ori_query_list[idx] = " ".join(tmp_list)

            break
        elif line.split(" ")[0] == "SELECT":
            new_query_list.append(line)
        elif idx != len(ori_query_list) - 1:
            if from_line != 0 and idx >= from_line:
                continue

            line = line.strip()

            if "," not in line:
                line += ","
                new_query_list.append(line)
                continue

            if line[0] == ",":
                line = line[1:] + ","
                new_query_list.append(line)
            else:
                new_query_list.append(line)
                
    common_idx = 1
    # query by line
    for line_num, line in enumerate(ori_query_list):
        dot_pos = line.find(",")

        if line[0] == ",":
            match_line = line[1:].strip()
        elif line[len(line) - 1] == ",":
            match_line = line[:len(line) - 1].strip()
        else:
            match_line = line.strip()

        # FN find
        if "FN_" in match_line:
            for col_name in col_list:
                if " AS " in match_line.upper():
                    if "FN_COMMONNAME" in match_line.upper():
                        regex = r"FN_COMMONNAME\(\s*'(.*?)'\s*,\s*(.*?)\s*\)\s*AS\s*(.*)"
                    else:
                        regex = r"FN_OBJECTNAME\(\s*'(.*?)'\s*,\s*(.*?)\s*\)\s*AS\s*(.*)"
                else:
                    if "FN_COMMONNAME" in match_line.upper():
                        regex = r"FN_COMMONNAME\(\s*'(.*?)'\s*,\s*(.*?)\s*\)\s*(.*)"
                    else:
                        regex = r"FN_OBJECTNAME\(\s*'(.*?)'\s*,\s*(.*?)\s*\)\s*(.*)"

                # match regex
                match = re.match(regex, match_line.upper())
                if match:
                    col_keyword = match.group(1).strip()
                    if "." not in match.group(2):
                        col_value = match.group(2).strip()
                    else:
                        mst_table_alias = match.group(2).strip().split(".")[0].strip()
                        col_value = match.group(2).strip().split(".")[1].strip()
                    col_name = match.group(3).strip()

                    if "AS " in col_name:
                        col_name = col_name.split(" ")[1].strip()

                    if col_name.upper() in match_line.upper():

                        if col_dict[col_keyword][0] == "A":
                            change_line = col_dict[col_keyword][1].format(common_idx, col_name)
                            change_cond = col_dict[col_keyword][2].format(common_idx, common_idx, mst_table_alias, col_value)
                        else:
                            change_line = str(col_dict[col_keyword][1].format(col_name)).replace("LS.", "LS{}.".format(common_idx))
                            change_cond = str(col_dict[col_keyword][2].format(common_idx, mst_table_alias, col_value)).replace("LS.", "LS{}.".format(common_idx))

                        common_idx += 1

                        new_cond_list.append(change_cond)
                        if line_num == from_line - 1:
                            new_query_list[line_num] = change_line
                        else:
                            new_query_list[line_num] = change_line + ","
                        break
        else:
            if line_num < from_line:
                continue
            elif line_num == from_line:
                if len(line.split(",")) > 1:
                    line = line.replace(",", " CROSS JOIN ")

                while "  " in line:
                    line = line.strip().replace("  ", " ")

                new_query_list.append(line)
            else:
                if line_num < where_line:
                    new_query_list += ori_query_list[from_line + 1:where_line]

                for cond in new_cond_list:
                    new_query_list.append(cond)

                new_query_list += ori_query_list[where_line:]
                break

    for line in new_query_list:
        print(line)
    print(";")


if __name__ == "__main__":
    main()
