def vertica_melt_test(dict_measure, dict_dates, t_name):

    #=====================================================#
    # Функция для чтения и формирования фильтров:
    #=====================================================#

    def read_filters(x):
    #----------------
        filters = ''
        f_filters = x.iloc[0]
    #----------------    
        try:
            ff = f_filters.split(';')
            for f in ff:
                filters = filters + '\n' + '  AND ' + f
        except:
            one = 1
    #----------------
        return filters
    
    #=====================================================#
    # Функция задающая поля агрегации для пивотов:
    #=====================================================#

    def agg_creater(x):
        agg_columns_tech = []
        for i in x:
            tech = '       ' + i + ','
            agg_columns_tech.append(tech)
        agg_col = '\n'.join(agg_columns_tech)
        return agg_col
    
    # Создание шкурки результирующией таблицы, для заполнения:
    query_start = '''DROP TABLE IF EXISTS table_1;
CREATE LOCAL TEMPORARY TABLE table_1
ON COMMIT PRESERVE ROWS AS

SELECT *
FROM {}
LIMIT 0;

SELECT ANALYZE_STATISTICS ('table_1');

/* ------------------------------------- */

DROP TABLE IF EXISTS result_table;
CREATE LOCAL TEMPORARY TABLE result_table ON COMMIT PRESERVE ROWS AS

SELECT *
FROM (
SELECT FactDate_301 AS FactDate,
{}
       '' AS metric,
       0 AS value
FROM table_1) AS a;
'''
    
    # Код наполнения результирующей таблицы мерами:
    query= '''
/* ------------------------------------- */

INSERT INTO result_table
SELECT {},
{}
       '{}',
       {}({})
FROM {}
WHERE 1=1
  AND FactDate IS NOT NULL{}
GROUP BY {}
HAVING 1=1
   AND {}({}) <> 0
   AND {}({}) IS NOT NULL;
   '''
    
    dict_measure = dict_measure.merge(dict_dates, how='left',on='date') # < -- добавляем кейсы с расчетными датами
    
    agg_columns = list(dict_measure['category_columns'].unique()) # <-- поля для агрегации
    agg_columns = [x for x in agg_columns if str(x) != 'nan']
    agg_col = agg_creater(agg_columns)
    
    order = ','.join(str(x+1) for x in range(len(agg_columns)+2))
    
    table_name = '{}'.format(t_name) # <-- введите сюда наименование таблицы (с указанием схемы, если это не темп сгенерированный выше)
    
    # чистим переменную хранящую готовую простыню
    result = ''
    
    # вставляем первую часть простыни
    result = result + query_start.format(table_name, agg_col)

    
    # цикл в котором создаются простыночки для каждой группы
    for index in dict_measure['new_name']:

        c_operator = dict_measure.loc[dict_measure['new_name'] == index]['operator'].iloc[0]
        c_measure = dict_measure.loc[dict_measure['new_name'] == index]['columns'].iloc[0]
        c_date = dict_measure.loc[dict_measure['new_name'] == index]['factdate'].iloc[0]

        total_filter = dict_measure.loc[dict_measure['new_name'] == index]['filter']
        c_filter = read_filters(total_filter)
        
        metric_result = query.format(c_date, 
                                     agg_col, 
                                     index, 
                                     c_operator, 
                                     c_measure, 
                                     table_name, 
                                     c_filter, 
                                     order,
                                     c_operator, 
                                     c_measure, 
                                     c_operator, 
                                     c_measure)
    
        result = result + metric_result
    return result


# Функция наводящая красоту в аутпуте работы готового скрипта
def query_runner_ddl_pohui(query,engine):
    
    import pandas as pd
    import sqlalchemy as sa
    from sqlalchemy import text
    from tenacity import retry, stop_after_attempt, wait_fixed
    from tqdm import tqdm

    query_runner_info = pd.DataFrame(query.replace('\n',' ').replace('\t',' ').split(';')[:-1])
    query_runner_info['query_run_flag'] = 0
    query_runner_info.columns = ['query','query_run_flag']
    
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def runner(run_data):
        
        filtered = run_data.loc[run_data['query_run_flag'] != 1]

        for index in tqdm(range(len(filtered))):
            query = filtered['query'].iloc[index]
            if query != '':
                with engine.connect().execution_options(autocommit=True) as connection:
                    connection.execute(text(query))
                    connection.commit()
                run_data.loc[run_data['query'] == query, 'query_run_flag'] = 1
                
            else: print('пук')
    
    runner(query_runner_info)