import os
import json
import objectpath
from openpyxl import load_workbook
from openpyxl import Workbook

ABSPATH = os.path.abspath(__file__)
# print(ABSPATH)
BASEPATH, current_filename = os.path.split(ABSPATH)
# print(BASEPATH)


def uNoGS_movie_method():

    json_path = os.path.join(BASEPATH, "uNoGS_Movie_JSON")
    # print(json_path)

    list_of_json = os.listdir(json_path)
    # print(list_of_json)

    released = []
    title = []
    type_ = []
    rating = []
    imdbid = []

    for i in range(1, len(list_of_json) + 1):
        # print(json_path+'\\'+str(i)+'.json')
        with open(json_path + "\\" + str(i) + ".json", "r") as r:
            read = json.load(r)
        # print(read)

        jsonnn_tree = objectpath.Tree(read["body"])

        released.append(list(jsonnn_tree.execute("$..released")))

        title.append(list(jsonnn_tree.execute("$..title")))

        type_.append(list(jsonnn_tree.execute("$..type")))

        rating.append(list(jsonnn_tree.execute("$..rating")))

        imdbid.append(list(jsonnn_tree.execute("$..imdbid")))

    print(released)
    print(title)
    print(type_)
    print(rating)
    print(imdbid)

    print(len(released))
    final_list = []
    for i in range(len(released)):
        for j in range(len(released[i])):
            # print(released[i][j])
            single_list = [released[i][j], title[i][j], type_[i][j], rating[i][j]]
            final_list.append(single_list)
    print(final_list)
    print(len(final_list))

    rk_final = [list(i) for i in set(map(tuple, final_list))]
    print(rk_final)
    print(len(rk_final))
    return rk_final
