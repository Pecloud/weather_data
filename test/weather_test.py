from interview import weather
import io


def test_replace_me():
    reader = io.StringIO("Station Name,Measurement Timestamp,Air Temperature\n\
                         Foster Weather Station,01/01/2016 11:00:00 PM,69\n\
Foster Weather Station,01/01/2016 08:00:00 PM,70\n\
Foster Weather Station,01/01/2016 07:00:00 PM,70\n\
Foster Weather Station,01/01/2016 06:00:00 PM,72\n\
Foster Weather Station,01/01/2016 05:00:00 PM,72\n\
Foster Weather Station,01/01/2016 04:00:00 PM,73\n\
Foster Weather Station,01/01/2016 03:00:00 PM,69\n\
Foster Weather Station,01/01/2016 02:00:00 PM,70\n\
Foster Weather Station,01/01/2016 01:00:00 PM,70\n\
Foster Weather Station,01/01/2016 12:00:00 PM,70\n\
Foster Weather Station,01/01/2016 11:00:00 AM,70\n\
Foster Weather Station,01/01/2016 10:00:00 AM,70\n\
Foster Weather Station,01/01/2016 09:00:00 AM,70\n\
Foster Weather Station,01/01/2016 08:00:00 AM,71\n\
Foster Weather Station,01/01/2016 07:00:00 AM,72\n\
Foster Weather Station,01/01/2016 06:00:00 AM,72\n\
Foster Weather Station,01/01/2016 05:00:00 AM,71\n\
Foster Weather Station,01/01/2016 04:00:00 AM,69\n\
Foster Weather Station,01/01/2016 03:00:00 AM,67\n\
Foster Weather Station,01/01/2016 02:00:00 AM,64\n\
Foster Weather Station,01/01/2016 01:00:00 AM,67\n\
Foster Weather Station,01/01/2016 12:00:00 AM,67\n")
    writer = io.StringIO()
    weather.process_csv(reader, writer)
    assert writer.getvalue() is not None
