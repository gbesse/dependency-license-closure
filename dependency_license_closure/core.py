import json,math
from .common import number,integer,identifier
OBLIGATIONS={'MIT':['notice'],'BSD-3-Clause':['notice','non_endorsement'],'ISC':['notice'],'Apache-2.0':['notice','state_changes','patent_terms'],'GPL-3.0-only':['notice','source_and_license_conditions'],'LGPL-3.0-only':['notice','relinking_and_source_conditions']}
def run(d):
 nodes=d['packages']
 if not isinstance(nodes,dict)or len(nodes)>50:raise ValueError('packages')
 root=identifier(d['root']);pending=[root];seen=set();order=[]
 while pending:
  k=pending.pop()
  if k in seen:continue
  if k not in nodes:raise ValueError('missing_dependency')
  identifier(k);seen.add(k);order.append(k);pending.extend(nodes[k]['dependencies'])
 options=[set()];unknown=set()
 for k in order:
  choices=nodes[k]['license_choices']
  if not isinstance(choices,list)or not choices:raise ValueError('choices')
  expanded=[]
  for choice in choices:
   if not isinstance(choice,list)or not choice:raise ValueError('conjunction')
   for license in choice:
    identifier(license)
    if license not in OBLIGATIONS:unknown.add(license)
   for prior in options:expanded.append(prior|set(choice))
  options=[set(v)for v in {tuple(sorted(v))for v in expanded}]
  if len(options)>512:raise ValueError('alternative_budget')
 return dict(reachable_packages=order,alternatives=[dict(licenses=sorted(v),declared_obligation_labels=sorted({o for license in v for o in OBLIGATIONS.get(license,[])}))for v in sorted(options,key=lambda v:sorted(v))],unknown_licenses=sorted(unknown),complete_declared_mapping=not unknown)
