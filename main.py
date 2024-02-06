from utils import read_file, get_country, sort_df, plot_barchart

def run_script():
    df = read_file()
    country = get_country(df)
    data = sort_df(df, country)
    plot_barchart(data, country)

if __name__ == "__main__":
    run_script()