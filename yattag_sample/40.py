def dump_html(args, results):

    doc = yattag.Doc()

    with doc.tag('style', type='text/css'):
        doc.asis(css)

    if not args.skip_class_metrics:
        for key, heading in CLASSIFICATION_METRICS:
            if results[key]:
                logging.info('Dumping "{}"'.format(heading))
                doc.line('h2', heading)
                ydump_metrics(doc, results[key])
                doc.stag('hr')

    if not args.skip_attribute_metrics and results['length']:  # TODO: clean up
        logging.info('Dumping Length')
        doc.line('h2', 'Length Inference')
        ydump_attrs(doc, results['length'])
        doc.stag('hr')
        logging.info('Dumping Tonnage')
        doc.line('h2', 'Tonnage Inference')
        ydump_attrs(doc, results['tonnage'])
        doc.stag('hr')
        logging.info('Dumping Engine Power')
        doc.line('h2', 'Engine Power Inference')
        ydump_attrs(doc, results['engine_power'])
        doc.stag('hr')
        logging.info('Dumping Crew Size')
        doc.line('h2', 'Crew Size Inference')
        ydump_attrs(doc, results['crew_size'])
        doc.stag('hr')

    # TODO: make localization results a class with __nonzero__ method
    if not args.skip_localisation_metrics and results[
            'localisation'].true_fishing_by_mmsi:
        logging.info('Dumping Localisation')
        doc.line('h2', 'Fishing Localisation')
        ydump_fishing_localisation(doc, results['localisation'])
        doc.stag('hr')

    with open(args.dest_path, 'w') as f:
        logging.info('Writing output')
        f.write(yattag.indent(doc.getvalue(), indent_text=True)) 
        