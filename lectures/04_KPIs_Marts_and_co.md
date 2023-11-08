# Lecture #4: KPIs, Data Marts, Online Analytical Processing

_November 8 2023_


## KPIs – Key Performance Indicators

* Meaningful mostly for high-level dashboards (reports)
* Better known as [KPIs](https://en.wikipedia.org/wiki/Performance_indicator)


## Data Mart

![DWH vs Data Mart](https://image.slidesharecdn.com/datamart-140405013513-phpapp02/95/data-mart-4-638.jpg?cb=1396661755)

* Typical end-users – business data analysts
* Usually department-specific set of analytical table sets, fed by the data warehouse
* See R. Kimball DWH Toolkit, or [Wikipedia](https://en.wikipedia.org/wiki/Data_mart)

## OLAP

![OLAP Illustration](https://i2.wp.com/olap.com/wp-content/uploads/2019/06/olap-3d-cube.png?resize=768%2C720&ssl=1)

* [Overview](https://en.wikipedia.org/wiki/Online_analytical_processing)
  - See all variants (MOLAP, ROLAP, HOLAP)
* Example implementations:
  - In Python:
    - [OlaPy](https://olapy.readthedocs.io/en/latest/)
    - [Cubes](https://en.wikipedia.org/wiki/Cubes_(OLAP_server))
  - SQL Server Analysis Services (see Kimball...)
  - [Elastic Search](https://stackoverflow.com/questions/35513249/reasons-against-using-elasticsearch-as-an-olap-cube)
