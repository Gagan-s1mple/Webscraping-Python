import pandas as pd


def fetch_nvd_data():
    """
    Fetches data from the National Vulnerability Database (NVD) website.

    This returns a DataFrame containing the scraped data.
    """
    try:
        # Load data from NVD website
        scraper = pd.read_html(
            'https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&search_type=all&isCpeNameSearch=false&hyperlink_types=CISA+Known+Exploited+Vulnerabilities')
        return scraper
    except Exception as e:
        print(f"Error occurred while fetching NVD data: {str(e)}")
        return None


def filter_critical_vulnerabilities(dataframe):
    """
    Filters critical vulnerabilities based on CVSS Severity and Summary.

    This returns filtered DataFrame with critical vulnerabilities.
    """
    try:
        # Assuming 'df' is defined earlier in your code
        filtered_df = dataframe[dataframe['Summary'].str.len() < 300]
        new_df = filtered_df[filtered_df["CVSS Severity"].str.contains("CRITICAL")]
        return new_df
    except Exception as e:
        print(f"Error occurred while filtering critical vulnerabilities: {str(e)}")
        return None


def main():
    nvd_data = fetch_nvd_data()

    if nvd_data is not None:
        for index, table in enumerate(nvd_data):
            print('-------------')
            print(f"Table {index}")
            print(table)

        filtered_data = filter_critical_vulnerabilities(df)
        if filtered_data is not None:
            print(filtered_data)
        else:
            print("No critical vulnerabilities found.")


if __name__ == "__main__":
    main()
