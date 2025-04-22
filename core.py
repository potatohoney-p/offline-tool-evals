def run(script,tools,max_calls=4,max_steps=8):
    if max_calls<0 or max_steps<0: raise ValueError('Negative budget')
    trace=[]; calls=0
    for number,step in enumerate(script):
        if number>=max_steps: return {'status':'step_budget','trace':trace,'answer':None}
        if not isinstance(step,dict): return {'status':'invalid_step','trace':trace,'answer':None}
        if step.get('kind')=='answer':
            if not isinstance(step.get('text'),str): return {'status':'invalid_answer','trace':trace,'answer':None}
            return {'status':'answered','trace':trace,'answer':step['text']}
        if step.get('kind')!='tool' or step.get('name') not in tools:
            return {'status':'denied','trace':trace,'answer':None}
        if calls>=max_calls: return {'status':'call_budget','trace':trace,'answer':None}
        args=step.get('args')
        if not isinstance(args,dict): return {'status':'invalid_arguments','trace':trace,'answer':None}
        calls+=1
        try: output=tools[step['name']](args)
        except (ValueError,TypeError,KeyError) as error:
            trace.append({'tool':step['name'],'ok':False,'error':type(error).__name__})
            return {'status':'tool_error','trace':trace,'answer':None}
        trace.append({'tool':step['name'],'ok':True,'output':output})
    return {'status':'no_answer','trace':trace,'answer':None}
def add_tool(args):
    if set(args)!=set(['a','b']) or any(isinstance(args[k],bool) or not isinstance(args[k],int) for k in args): raise ValueError('Two integer operands required')
    return args['a']+args['b']
