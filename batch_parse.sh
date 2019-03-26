#! /bin/sh
PCLC_FILES=$(ls ./xml/pclc)
SPEC_FILES=$(ls ./xml/spec)

for PCLC in $PCLC_FILES
do
        python xmlparser.py -r f -c pc ./xml/pclc/$PCLC
done

for SPEC in $SPEC_FILES
do
        python xmlparser.py -r tgsp -a f ./xml/spec/$SPEC
done
