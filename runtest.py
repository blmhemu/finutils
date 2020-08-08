from finutils import CachedReader
from datetime import date


def test_finutils():
    scrips = ["PVR.NS", "LT.NS", "INFY.NS"]
    cr = CachedReader("yahoo", "./data")
    df1 = cr.get_data(scrips[0], "2010-1-1", "2020-6-1")
    df2 = cr.get_data(scrips[1], date(2010, 1, 1), date(2020, 6, 1))
    df3 = cr.get_data(scrips[2])

    # print(df1, df2, df3)
    if not (df1.empty or df2.empty or df3.empty) and all(
        cr.scrip_file_exists(cr.get_scrip_file_path(scrip)) for scrip in scrips
    ):
        print("OK")


if __name__ == "__main__":
    test_finutils()
