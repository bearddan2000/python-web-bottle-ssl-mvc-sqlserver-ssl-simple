# python-web-bottle-ssl-mvc-sqlserver-ssl-simple

## Description
Simple web app that serves static pages
for a bottle project.

Uses sqlalchemy query a table `dog`.

Is a self signed ssl

Sql server uses self-signed ssl.

## Tech stack
- python
  - bottle
  - sqlalchemy
  - beaker
  - cheroot
- bootstrap
- jquery
- dataTable
- mssql
- ssl

## Docker stack
- alpine:edge
- alpine:edge
- python:latest
- mcr.microsoft.com/mssql/server:2017-CU17-ubuntu

## To run
`sudo ./install.sh -u`
- [Availble at](https://localhost)

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
[Bottle sqlalchemy setup](https://github.com/iurisilvio/bottle-sqlalchemy/blob/master/examples/basic.py)
