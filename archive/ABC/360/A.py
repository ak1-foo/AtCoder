table_items = input()

R_idx = table_items.find('R')
M_idx = table_items.find('M')

if (R_idx < M_idx):
    print('Yes')
else:
    print('No')
