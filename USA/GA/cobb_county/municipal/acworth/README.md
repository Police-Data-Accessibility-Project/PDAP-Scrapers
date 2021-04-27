This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate
For example "daily at 8pm EST" or "every Friday, usually before noon"

## Legal
https://acworthpolice.org/robots.txt   No specific delay needed.

Don't see any terms of service on the page.

# Fields to collect:
_Move these fields to the appropriate list below when you submit your scraper._

## Fields unobtainable within our legal guidelines:

## Fields not available:
* _id
* _state
* _county
* CaseNum
* FirstName
* MiddleName
* LastName
* Suffix
* DOB
* Sex
* ArrestDate
* FilingDate
* OffenseDate
* DivisionName
* CaseStatus
* DefenseAttorney
* PublicDefender
* Judge
* ChargeCount
* ChargeStatute
* ChargeDescription
* ChargeDisposition
* ChargeDispositionDate
* ChargeOffenseDate
* ChargeCitationNum
* ChargePlea
* ChargePleaDate
* ArrestingOfficer
* ArrestingOfficerBadgeNumber
* BookingNum
* BookingDate
* WarrantNum
* BailAmount
* SearchIncident

## Fields being collected:
* Race

## Fields available not present on the list above:

## Data uniformity
Unsure on the type of data, annual reports

# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.
