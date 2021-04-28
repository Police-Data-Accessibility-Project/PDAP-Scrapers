This readme should give people everything they need to maintain the scraper.

Please stick to [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) when modifying this readme.  

Note: Ensure your scraper calls the etl.py file. Even if there is nothing in there now, the scraped data will need to be loaded into our database and the etl.py file is what will handle that!

# Source info
Be sure to [update the dataset](https://www.dolthub.com/repositories/pdap/datasets) if there's anything that should be stored there.

The UOF contains the fields listed below, along with demographics such as sex, race, years of service, age, rank.

There are also UOF to the type of call, division, zones, time of day (day, evening, and morning watch)

List of videos to UOF categorized by BWC (body worn camera), taser (taser camera?), and none.

## Data refresh rate
Cobra weekly PDF updates Saturdays at 24:00 (at least that is the data range within)

UOF likely updates yearly/any time their policy changes.

## Legal
Nope

# Fields to collect:
_Move these fields to the appropriate list below when you submit your scraper._

## Fields unobtainable within our legal guidelines:

## Fields not available:
* _id
* _state
* _county
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

## Fields being collected:
  ### Cobra/weekly:
  * CaseNum; as ReportNumber
  * Rest are NotInList

## Fields available not present on the list above:
  ### Use of Force complaints:
  * IncidentIANum; Probably internal affairs number
  * IncidentOpenDate
  * Allegation
  * OfficerFirstName; Only first letter
  * OfficerLastName
  * OfficerRace
  * OfficerSex
  #### Firearm discharge:
  * OfficerFirstName; Only first letter
  * Date
  * FileNumber; Can likely rename IncidentIANum to FileNum
  * IncidentLocation
  * SuspectStatus; Injured/Deceased
  * SuspectRace/SuspectGender; In this format
  * OfficerRace/OfficerGender; In this format

### Officer demographics:
  * OfficerRace
  * OfficerSex
  * OfficerAge
  * OfficerRank

### Injured suspect demographics
  * SuspectRace
  * SuspectGender

## Cobra/Weekly:
  * BeingCollected (first time using this, means that it's in the collected category)
  * Report Date
  * Occur Date
  * Occur Time
  * Possible Date
  * Possible Time
  * Beat
  * Aparment office prefix
  * ApartmentNumber
  * Location
  * Shift Occurence; spelling copied from csv
  * Location Type
  * UCR Literal
  * UCR #
  * IBR Code
  * Neighborhood
  * NPU
  * Latitude
  * Longitude


## Data uniformity
Are cases or records numbered in a consistent (or inconsistent) way that might be helpful to note?

# Sample response
in `./data/`
