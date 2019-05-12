import re


def main():
    operator = ['+', '-', '*', '/', '']
    for i in range(1000, 10000):
        str_i = format(i)
        rev_str_i = str_i[::-1]
        for op_1 in operator:
            if op_1 == '/' and str_i[1] == '0':
                continue
            for op_2 in operator:
                if op_2 == '/' and str_i[2] == '0':
                    continue
                for op_3 in operator:
                    if op_3 == '/' and str_i[3] == '0':
                        continue
                    formula = str_i[0] + op_1 + str_i[1] + op_2 + str_i[2] + op_3 + str_i[3]
                    # print(formula)
                    ope_list = re.findall(r'\D', formula)   # 演算子のみ抽出
                    num_list = re.split(r'\D', formula)     # 数字のみ抽出
                    n_list = [str(int(n)) for n in num_list]    # 数字を数値に変換（先頭0をなくすため）
                    for index, ope in enumerate(ope_list):
                        n_list.insert(index + index + 1, ope)     # 数字リストの合間に演算子を追加
                    # print(n_list)
                    s_text = ''
                    for item in n_list:
                        s_text += item  # 数式を作成
                    # print(str_i)
                    # print(rev_str_i)
                    # print(s_text)
                    # print(eval(s_text))
                    if len(s_text) > 4:     # 演算子なしは除外
                        if rev_str_i == format(eval(s_text)):
                            print('true: {}, {}, {}, {}'.format(str_i, rev_str_i, s_text, eval(s_text)))


if __name__ == '__main__':
    main()
