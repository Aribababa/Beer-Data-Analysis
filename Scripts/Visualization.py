import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set(color_codes=True)


class DataVisualization:

    def __init__(self, path="", categoty=""):

        self.DefeaultPath = path + '/' + categoty
        self.data = []
        self.dataframe = None
        self.color_index = 0
        return

    def add_data(self, retrieved_data):
        self.data.extend(retrieved_data)
        return

    def create_dataframe(self):
        self.dataframe = pd.DataFrame(self.data)
        return


    def data_missingness_matrix(self):

        import missingno as msno

        msno.matrix(self.dataframe)
        plt.title("Missingness matrix of the data")

        # Guardamos la imagen y quitamos los cambios que se realizaron.
        plt.savefig(self.DefeaultPath + " missigness matrix.png")
        plt.cla()
        plt.clf()

        return

    def data_heatmap(self):

        sns.heatmap(self.dataframe)

        # Guardamos la imagen y quitamos los cambios que se realizaron.
        plt.savefig(self.DefeaultPath + " heatmap.png")
        plt.cla()
        plt.clf()

        return

    @staticmethod
    def beer_count_per_style(histogram_dict, path, limit=20):

        plt.figure(figsize=(18, 9))
        styles_count_dataframe = pd.DataFrame(histogram_dict.items(), columns=['Style', 'Count'])
        styles_query = styles_count_dataframe.groupby(
            ['Style']).sum()[['Count']].sort_values(['Count'], ascending=False).reset_index()[:limit]

        sns.barplot(x='Count', y='Style', data=styles_query.reset_index())

        plt.ylabel("Style", fontsize=16)
        plt.xlabel("Beers per style", fontsize=16)
        plt.title(str(limit) + ' most popular Styles', fontsize=22)

        # Guardamos la imagen y quitamos los cambios que se realizaron.
        plt.savefig(path + "/Crafted beer style histogram.png", dpi=200)
        plt.cla()
        plt.clf()

        print "Beer Style histogra saved on " + path
        return

    @staticmethod
    def percentaje_per_style(histogram_dict, path, limit=10):

        import operator

        histogram_dict = sorted(histogram_dict.items(), key=operator.itemgetter(1, 0), reverse=True)
        list_keys, list_values = map(list, zip(*histogram_dict))

        # lo que esta fuera de los limites se considera como otros, por lo que adaptamos la lista.
        other_values = sum(list_values[limit:])

        # separamos en dos listas
        list_keys = list_keys[:limit]
        list_values = list_values[:limit]

        list_keys.append('Others')
        list_values.append(other_values)

        # Adaptamos los datos para poder graficarlos en la grafica de pastel
        total = float(sum(list_values))
        sizes = [100 * (x / total) for x in list_values]

        # Comenzamos a graficar el resultado
        plt.style.use('seaborn')
        _, ax1 = plt.subplots()

        # colors
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, colors=colors, labels=list_keys, autopct='%1.1f%%', startangle=90)

        # draw circle
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)

        # Equal aspect ratio ensures that pie is drawn as a circle
        ax1.axis('equal')
        plt.title("Ratio of the styles in the beer data set")
        plt.tight_layout()

        # Guardamos la imagen y quitamos los cambios que se realizaron.
        plt.savefig(path + "/Crafted beer style piechart.png", dpi=200)
        plt.cla()
        plt.clf()

        print "Percentaje per style Piechart saved on " + path

        return

    @staticmethod
    def percentage_abv(histogram_dict, path, limit=20):

        import numpy as np
        for key, values in histogram_dict.iteritems():
            histogram_dict[key] = np.mean(histogram_dict[key], dtype=float)

        plt.figure(figsize=(18, 9))
        styles_count_dataframe = pd.DataFrame(histogram_dict.items(), columns=['Style', 'ABV'])
        styles_query = styles_count_dataframe.groupby(
            ['Style']).sum()[['ABV']].sort_values(['ABV'], ascending=False).reset_index()[:limit]

        sns.barplot(x='ABV', y='Style', data=styles_query.reset_index())

        plt.ylabel("Style", fontsize=16)
        plt.xlabel("Alcohol By Volume(%)", fontsize=16)
        plt.title(str(limit) + ' Stronger Styles', fontsize=22)

        # Guardamos la imagen y quitamos los cambios que se realizaron.
        plt.savefig(path + "/Crafted beer ABV histogram.png", dpi=200)
        plt.cla()
        plt.clf()

        print "Beer Style histogra saved on " + path
        return

    def data_correlation(self, keys):

        color_pallete = ['b', 'y', 'c', 'm', 'g']

        try:
            correlation_plot = self.dataframe.loc[:, keys]
            sns.regplot(x=keys[0], y=keys[1], data=correlation_plot, color=color_pallete[self.color_index])
            self.color_index = (self.color_index + 1) % 5
            plt.title("Correlation between " + keys[0] + " and " + keys[1])

            # Guardamos la imagen y quitamos los cambios que se realizaron.
            plt.savefig(self.DefeaultPath + " " + keys[0] + " and " + keys[1] + " correlation.png", dpi=200)
            plt.cla()
            plt.clf()

        except KeyError:
            print "Bad key or keys for the Dataframe."

        return self.dataframe[keys[1]].corr(self.dataframe[keys[0]], method='pearson')

    def data_distribution(self, key):

        color_pallete = ['b', 'y', 'c', 'm', 'g']

        try:
            distribution_plot = self.dataframe.loc[:, key]
            sns.distplot(distribution_plot, color=color_pallete[self.color_index])
            self.color_index = (self.color_index + 1) % 5
            plt.title(key + " Distribution")
            plt.ylabel('Normed Frequency', fontsize=15)
            plt.xlabel(key, fontsize=15)

            # Guardamos la imagen y quitamos los cambios que se realizaron.
            plt.savefig(self.DefeaultPath + " " + key + " distribution.png", dpi=200)
            plt.cla()
            plt.clf()

        except KeyError:
            print "Bad key or keys for the Dataframe."

        return

    def data_box_plot(self):
        return

    def data_feature_importance(self, features_list, title="Feature Importance"):

        from sklearn.preprocessing import LabelEncoder, Imputer
        from sklearn.cross_validation import train_test_split

        # extraemos las columnas con los features
        clf_data = self.dataframe.loc[:, features_list]

        # Preprocesaos los datos y los ajustamos
        cat_feats_to_use = list(clf_data.select_dtypes(include=object).columns)
        for feat in cat_feats_to_use:
            encoder = LabelEncoder()
            clf_data[feat] = encoder.fit_transform(clf_data[feat])

        # Llenamos los valores vacios
        num_feats_to_use = list(clf_data.select_dtypes(exclude=object).columns)
        for feat in num_feats_to_use:
            imputer = Imputer(strategy='median')
            clf_data[feat] = imputer.fit_transform(clf_data[feat].values.reshape(-1, 1))

        # Separamos el index de loas Fetures
        X = clf_data.iloc[:, 1:]
        y = clf_data.iloc[:, 0]  # the target were the first column I included

        # Entrenamos con los datos recivido
        x_train, _, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=35)

        from sklearn.preprocessing import StandardScaler

        scaler = StandardScaler()
        x_train = scaler.fit_transform(x_train)

        from sklearn.ensemble.forest import RandomForestClassifier

        # inicializamos el clasificador
        clf = RandomForestClassifier(n_estimators=8, random_state=34)
        clf.fit(x_train, y_train)

        # Pasamos los datos a un Dataframe para poder graficarlos
        feats_imp = pd.DataFrame(clf.feature_importances_, index=X.columns, columns=['FeatureImportance'])
        feats_imp = feats_imp.sort_values('FeatureImportance', ascending=False)

        feats_imp.plot(kind='barh', figsize=(12, 6), legend=False)
        plt.title(title)
        sns.despine(left=True, bottom=True)
        plt.gca().invert_yaxis()

        plt.savefig(self.DefeaultPath + " feature importance.png", dpi=200)
        plt.cla()
        plt.clf()

        return
