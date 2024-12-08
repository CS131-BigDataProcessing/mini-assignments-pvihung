#!/usr/bin/env nextflow

process uppercase {
    // Declare the input and output
    input:
    val params.input_string
    path output_file = params.output_file

    output:
    path output_file

    // Script to run
    script:
    """
    echo "$input_string" | tr '[:lower:]' '[:upper:]' > $output_file
    """
}

workflow {
    // Run the uppercase process
    uppercase()
}

