## ### VDAs em atraso

#### Importa bibliotecas e define nome dos arquivos

import pandas as pd
import os
from datetime import datetime

# Define os caminhos dos arquivos
vda_path = 'C:\\Users\\ELXY\\Documents\\Codigos\\Python\\P84_85\\LDs\\TodasVDAs\\'
ld_path = 'C:\\Users\\ELXY\\Documents\\Codigos\\Python\\P84_85\\LDs\\'

# Get today's date and format it as YY.MM.DD
today = datetime.now()
vda_file = f"VDA {today.strftime('%y.%m.%d')}.xlsx"
ld_file = 'LD_comment_combined.xlsx'
vda_updated_file = f"VDA {today.strftime('%y.%m.%d')}_updated.xlsx"
vda_updated_file_op = f"VDA {today.strftime('%y.%m.%d')}_updated_op.xlsx"

#### Analisa se o documento existe na LD consolidada.
#- Verifica se cada documento referênciado nas VDAs tem sua correspondência na LD Consolidada.
#- Verifica se existem comentários (YES/NO) nesses documentos.
#- Verifica também qual a Discipline do documento.

# Carregar os arquivos Excel
vda_df = pd.read_excel(os.path.join(os.path.dirname(vda_path), vda_file), sheet_name="DADOS")
ld_df = pd.read_excel(os.path.join(os.path.dirname(ld_path), ld_file), sheet_name="LD")

# Criar as novas colunas no DataFrame VDA
vda_df['Discipline'] = ''
vda_df['Comments_new'] = ''

# Iterar sobre as linhas do DataFrame VDA
for index, row in vda_df.iterrows():
    ref_doc = row['REFERENCE DOCUMENT NAME']
    
    # Procurar o documento correspondente no DataFrame LD
    matching_row = ld_df[ld_df['CLIENT_DOCUMENT'] == ref_doc]
    
    if not matching_row.empty:
        # Se encontrou uma correspondência
        vda_df.at[index, 'Discipline'] = matching_row['Discipline'].values[0]
        
        if pd.notna(matching_row['Comments_new'].values[0]):
            vda_df.at[index, 'Comments_new'] = matching_row['Comments_new'].values[0]
        else:
            vda_df.at[index, 'Comments_new'] = 'NO'
    else:
        # Se não encontrou correspondência
        vda_df.at[index, 'Comments_new'] = 'Documento não encontrado na LD_comment_combined.xlsx'

# Remover linhas duplicadas com base na coluna "VDA NAME"
if "VDA NAME" in vda_df.columns and "VDA VERSION" in vda_df.columns:
    print(f"Número de linhas antes da remoção de duplicatas: {len(vda_df)}")
    # Sort by VDA VERSION in descending order and keep first occurrence of each VDA NAME
    vda_df = vda_df.sort_values('VDA VERSION', ascending=False).drop_duplicates(subset='VDA NAME', keep='first')
    print(f"Número de linhas após a remoção de duplicatas: {len(vda_df)}")
else:
    print("Aviso: Colunas necessárias não encontradas. Não foi possível remover duplicatas.")


# Cria uma máscara contendo 'ELECTRICAL' ou 'ELETRICA' na 'Discipline'
electrical_mask = vda_df['Discipline'].str.contains('ELECTRICAL|ELETRICA|ELÉTRICA', case=False, na=False)
# Cria um novo dataframe com as linhas filtradas
df_electrical = vda_df[electrical_mask]
# Manter somente as linhas do dataframe df_electrical onde a coluna '>8WORKING DAYS' é igual a 'x'
df_electrical = df_electrical[df_electrical['>8WORKING DAYS'].str.lower() == 'x']
# Reset index
df_electrical.reset_index(drop=True, inplace=True)

# Cria uma máscara contendo AUTOMATION|INSTRUMENTATION|INSTRUMENTAÇÃO na 'Discipline'
automation_mask = vda_df['Discipline'].str.contains('AUTOMATION|AUTOMAÇÃO|A&I|INSTRUMENTATION|INSTRUMENTAÇÃO|AUT&INST', case=False, na=False)
# Cria um novo dataframe com as linhas filtradas
df_automation = vda_df[automation_mask]
# Manter somente as linhas do dataframe df_automation onde a coluna '>8WORKING DAYS' é igual a 'x'
df_automation = df_automation[df_automation['>8WORKING DAYS'].str.lower() == 'x']
# Reset index
df_automation.reset_index(drop=True, inplace=True)

# Cria uma máscara contendo 'STATIC|ESTATICO|ESTÁTICO' na 'Discipline'
static_mask = vda_df['Discipline'].str.contains('STATIC|ESTATICO|ESTÁTICO', case=False, na=False)
# Cria um novo dataframe com as linhas filtradas
df_static = vda_df[static_mask]
# Manter somente as linhas do dataframe df_static onde a coluna '>8WORKING DAYS' é igual a 'x'
df_static = df_static[df_static['>8WORKING DAYS'].str.lower() == 'x']
# Reset index
df_static.reset_index(drop=True, inplace=True)

# Cria uma máscara contendo 'PIPING|TUBULAÇÃO' na 'Discipline'
piping_mask = vda_df['Discipline'].str.contains('PIPING|TUBULAÇÃO', case=False, na=False)
# Cria um novo dataframe com as linhas filtradas
df_piping = vda_df[piping_mask]
# Manter somente as linhas do dataframe df_piping onde a coluna '>8WORKING DAYS' é igual a 'x'
df_piping = df_piping[df_piping['>8WORKING DAYS'].str.lower() == 'x']
# Reset index
df_piping.reset_index(drop=True, inplace=True)

# Cria uma máscara contendo 'TELECOM|TELECOMUNICAÇÃO|TELECOMUNICAÇÕES' na 'Discipline'
telecom_mask = vda_df['Discipline'].str.contains('TELECOM|TELECOMUNICAÇÃO|TELECOMUNICAÇÕES', case=False, na=False)
# Cria um novo dataframe com as linhas filtradas
df_telecom = vda_df[telecom_mask]
# Manter somente as linhas do dataframe df_telecom onde a coluna '>8WORKING DAYS' é igual a 'x'
df_telecom = df_telecom[df_telecom['>8WORKING DAYS'].str.lower() == 'x']
# Reset index
df_telecom.reset_index(drop=True, inplace=True)

# Cria uma máscara contendo 'OPERATION|UN|OPERAÇÃO' na 'Discipline'
operation_mask = vda_df['Discipline'].str.contains('OPERATION|UN|OPERAÇÃO', case=False, na=False)
# Cria um novo dataframe com as linhas filtradas
df_operation = vda_df[operation_mask]
# Manter somente as linhas do dataframe df_operation onde a coluna '>8WORKING DAYS' é igual a 'x'
df_operation = df_operation[df_operation['>8WORKING DAYS'].str.lower() == 'x']
# Reset index
df_operation.reset_index(drop=True, inplace=True)

# Cria uma máscara contendo 'COMISSIONING|EICOM|COMM|COMISSIONAMENTO' na 'Discipline'
commissioning_mask = vda_df['Discipline'].str.contains('COMISSIONING|EICOM|COMM|COMISSIONAMENTO', case=False, na=False)
# Cria um novo dataframe com as linhas filtradas
df_commissioning = vda_df[commissioning_mask]
# Manter somente as linhas do dataframe df_commissioning onde a coluna '>8WORKING DAYS' é igual a 'x'
df_commissioning = df_commissioning[df_commissioning['>8WORKING DAYS'].str.lower() == 'x']
# Reset index
df_commissioning.reset_index(drop=True, inplace=True)

# Salvar o DataFrame VDA atualizado
output_path = os.path.join(os.path.dirname(vda_path), vda_updated_file)

with pd.ExcelWriter(output_path) as writer:
    vda_df.to_excel(writer, sheet_name='VDA', index=False)
    df_electrical.to_excel(writer, sheet_name='Eletrica', index=False)
    df_automation.to_excel(writer, sheet_name='Automation', index=False)
    df_static.to_excel(writer, sheet_name='Static', index=False)
    df_piping.to_excel(writer, sheet_name='Piping', index=False)
    df_telecom.to_excel(writer, sheet_name='Telecom', index=False)
    df_operation.to_excel(writer, sheet_name='Operation', index=False)
    df_commissioning.to_excel(writer, sheet_name='Commissioning', index=False)

print(f"Arquivo atualizado salvo em: {output_path}")

# Cria uma máscara onde a coluna 'Discipline' é exatamente igual a "OPERATION", "UN" ou "OPERAÇÃO"
operation_mask_2 = vda_df['Discipline'].str.strip().str.upper().isin(['OPERATION', 'UN', 'OPERAÇÃO'])
# Cria um novo dataframe com as linhas filtradas
df_operation_2 = vda_df[operation_mask_2]
# Manter somente as linhas do dataframe df_operation_2 onde a coluna '>8WORKING DAYS' é igual a 'x'
df_operation_2 = df_operation_2[df_operation_2['>8WORKING DAYS'].str.lower() == 'x']
# Reset index
df_operation_2.reset_index(drop=True, inplace=True)

# Cria uma máscara contendo 'COMISSIONING|EICOM|COMM|COMISSIONAMENTO' na 'Discipline'
not_find_mask = vda_df['Comments_new'].str.contains('NO|Documento não encontrado na LD_comment_combined.xlsx', case=False, na=False)
# Cria um novo dataframe com as linhas filtradas
df_not_find = vda_df[not_find_mask]
# Manter somente as linhas do dataframe df_commissioning onde a coluna '>8WORKING DAYS' é igual a 'x'
df_not_find = df_not_find[df_not_find['>8WORKING DAYS'].str.lower() == 'x']
# Reset index
df_not_find.reset_index(drop=True, inplace=True)

# Salvar o DataFrame VDA atualizado
output_path = os.path.join(os.path.dirname(vda_path), vda_updated_file_op)

with pd.ExcelWriter(output_path) as writer:
    df_operation_2.to_excel(writer, sheet_name='Operation', index=False)
    df_not_find.to_excel(writer, sheet_name='No_Not_Find', index=False)

print(f"Arquivo atualizado salvo em: {output_path}")
