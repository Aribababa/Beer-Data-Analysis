from Database import MongoDatabase
from Visualization import DataVisualization
import Processing
import json


CRAFTED_BEER_SETS = 73  # Numero de colecciones que se van a evaluar


def main():

    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)
    warnings.simplefilter(action='ignore', category=DeprecationWarning)

    visualization = DataVisualization(path="../Results", categoty="Crafted beer")

    crafted_beer_db = MongoDatabase('mongodb://localhost:27017/', 'Artisanal-beer')
    style_histogram = {}
    abv_style_stats = {}

    for i in range(0, CRAFTED_BEER_SETS):
        retrieved_data = crafted_beer_db.fetch_collection('Artisanal-beer-' + str(i))
        visualization.add_data(retrieved_data)

        # Ranking de los estilos de cerveza mas comunes
        style_histogram = Processing.data_histogram(retrieved_data, 'Style', histogram=style_histogram)
        abv_style_stats = Processing.data_accumulation(retrieved_data, 'Style',  'ABV', accumulation=abv_style_stats)

    # visualization.create_dataframe()    # Prepramos los datos para visulizarlos
    style_histogram.pop("N/A")  # Quitamos los valores no validos del histogrma
    abv_style_stats.pop("N/A")  # Quitamos los valores no validos del histogrma

    # Analizamos la consistencia de los datos
    # visualization.data_missingness_matrix()

    # Obtenemos alfunas estadisticas de los estilos
    # DataVisualization.percentaje_per_style(style_histogram, "../Results")
    # DataVisualization.beer_count_per_style(style_histogram, "../Results")
    DataVisualization.percentage_abv(abv_style_stats, "../Results")

    # Obtenemos las distribuciones de algunos parametros.
    # visualization.data_distribution('ABV')
    # visualization.data_distribution('Color')
    # visualization.data_distribution('IBU')
    # visualization.data_distribution('OG')
    # visualization.data_distribution('FG')
    # visualization.data_distribution('Efficiency')
    # visualization.data_distribution('BrewMethod')

    # Calculamos las correlaciones de algunos parametros.
    # print "Correlation between ABV and Color: " + str(visualization.data_correlation(['ABV', 'Color']))
    # print "Correlation between IBU and Color: " + str(visualization.data_correlation(['IBU', 'Color']))
    # print "Correlation between OG and Color : " + str(visualization.data_correlation(['OG', 'Color']))
    # print "Correlation between FG and Color : " + str(visualization.data_correlation(['FG', 'Color']))
    # print "Correlation between BoilGravity and Color : " + str(visualization.data_correlation(['BoilGravity', 'Color']))

    # print "Correlation between IBU and ABV : " + str(visualization.data_correlation(['IBU', 'ABV']))
    # print "Correlation between OG and ABV : " + str(visualization.data_correlation(['OG', 'ABV']))
    # print "Correlation between FG and ABV : " + str(visualization.data_correlation(['FG', 'ABV']))
    # print "Correlation between Efficiency and ABV : " + str(visualization.data_correlation(['Efficiency', 'ABV']))

    # print "Correlation between FG and OG : " + str(visualization.data_correlation(['FG', 'OG']))

    # Obtenemos las features mas impoortantes de las cerveza.
    #visualization.data_feature_importance([
    #    'StyleID', 'Style', 'ABV', 'IBU', 'Color', 'Size(L)', 'BrewMethod',
    #    'PitchRate', 'MashThickness'
    #], title="Most important features on Crfated Beer")

    return


if __name__ == '__main__':
    main()
