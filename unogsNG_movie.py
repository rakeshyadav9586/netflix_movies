import os
import json
import objectpath
import requests
from openpyxl import load_workbook
from openpyxl import Workbook

ABSPATH = os.path.abspath(__file__)
# print(ABSPATH)
BASEPATH, current_filename = os.path.split(ABSPATH)
# print(BASEPATH)


def unogsNG_movie():

    json_path = os.path.join(BASEPATH, "unogsNG_Movie_JSON")
    print(json_path)

    list_of_json = os.listdir(json_path)
    print(list_of_json)

    released = []
    title = []
    type_ = []
    imdbid = []

    for i in range(1, len(list_of_json) + 1):
        print(json_path + "\\" + str(i) + ".json")
        with open(json_path + "\\" + str(i) + ".json", "r", encoding="utf8") as r:
            read = json.load(r)
        print(read)

        jsonnn_tree = objectpath.Tree(read["body"])
        released.append(list(jsonnn_tree.execute("$..year")))

        title.append(list(jsonnn_tree.execute("$..title")))

        type_.append(list(jsonnn_tree.execute("$..vtype")))

        imdbid.append(list(jsonnn_tree.execute("$..imdbid")))

    print(len(released))
    print(released)
    print(title)
    print(type_)
    print(imdbid)

    final_list = []
    for i in range(len(released)):
        for j in range(len(released[i])):
            print(imdbid[i][j])
            rating = []
            rating_votes = []
            url = (
                "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/"
                + imdbid[i][j]
            )
            # print(url)
            headers = {
                "x-rapidapi-host": "imdb-internet-movie-database-unofficial.p.rapidapi.com",
                "x-rapidapi-key": "add your key",
            }

            response = requests.request("GET", url, headers=headers)

            r = response.text
            # print(r)
            read = json.loads(r)
            rating = read["rating"]
            print(rating)
            rating_votes = read["rating_votes"]
            print(rating_votes)

            if (rating and rating_votes) and int(rating_votes) >= 50000:
                print("if loop" + str(j))

                single_list = [str(released[i][j]), title[i][j], type_[i][j], rating]
                final_list.append(single_list)

    print(final_list)
    print(len(final_list))

    rk_final = [list(i) for i in set(map(tuple, final_list))]
    print(rk_final)
    print(len(rk_final))
    return rk_final
