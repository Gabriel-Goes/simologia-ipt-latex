def generate_map_latex(output_filename):
    latex_code = r"""
\begin{figure}[ht!]
    \centering
	\captionsetup{justification=justified, singlelinecheck=false, width=1\textwidth}
    \caption{Mapa da região de interesse no entorno do empreendimento, mostrando as principais cidades, rodovias e rios, com a localização das pedreiras, estações \textbf{BCM2} e \textbf{MC9}, e eventos próximos ao empreendimento detectados no período de interesse.}
    \includegraphics[width=0.8\textwidth]{./boletim/baesa/figuras/mapa_baesa.png}
    \caption*{Fonte: IPT}
\end{figure}
"""
    with open(output_filename, "w") as output_file:
        output_file.write(latex_code)


generate_map_latex("./boletim/baesa/tex/mapa_baesa.tex")