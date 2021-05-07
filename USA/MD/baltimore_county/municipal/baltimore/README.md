This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

## Data refresh rate
For example "daily at 8pm EST" or "every Friday, usually before noon"

## Legal
Include the Terms of Service (or link to them). Is there anything else we should know?

# Fields to collect:
_Move these fields to the appropriate list below when you submit your scraper._

* _id
* _state
* _county
* CaseNum
* FirstName
* MiddleName
* LastName
* Suffix
* DOB
* Race
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

## Fields unobtainable within our legal guidelines:

## Fields not available:

## Fields being collected:
### Calls for service:
* recordId
* callKey
* callDateTime
* priority
* district
* description
* callNumber
* incidentLocation
* location
* Neighborhood
* PoliceDistrict
* PolicePost
* CouncilDistrict
* SheriffDistricts
* Community_Statistical_Areas
* Census_Tracts
* VRIZones
* ZIPCode
* NeedsSync
* IsDeleted
* ESRI_OID

## Arrests:
RowID
ArrestNumber
Age
Gender
Race
ArrestDateTime
ArrestLocation
IncidentOffence
IncidentLocation
Charge
ChargeDescription
District
Post
Neighborhood
Latitude
Longitude
GeoLocation


## Fields available not present on the list above:

## Fields not collected:
* RowID (Not useful for us)
* Latitude (redundant, in GeoLocation)
* Longitude (redundant, in GeoLocation)
* Geometry (not sure what it's for)

## Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?

# Sample response
In the folder, include a JSON payload, a PDF, or anything that is representative of what kind of data we get back when we run this scraper. Truncate it if necessary.
