# Задание 44 |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |

enc = OneHotEncoder()
enc.fit(data[['whoAmI']])

one_hot = enc.transform(data[['whoAmI']])
cols = enc.get_feature_names_out(['whoAmI'])

one_hot_df = pd.DataFrame(one_hot.toarray(), columns=cols)
print(one_hot_df.head())