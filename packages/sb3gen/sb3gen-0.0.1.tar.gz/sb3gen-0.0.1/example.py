import sb3gen.blocks as b
import sb3gen.targets as t
import sb3gen.project as p

# Create stage
stage = t.Stage()
# Create main script
script = b.Script(b.StackBlock("event_whenflagclicked", {}, {}, top=True))
# Create variable `var`
v = stage.create_variable("var", "value")
# Create list `list`
l = stage.create_list("list", ["example"])
# Create and push (1 + 1) block
inner = script.push_op(b.OpBlock("operator_add", {"NUM1": b.BlockInput(b.ScratchValue(1), True),"NUM2": b.BlockInput(b.ScratchValue(1), True)}, {}))
# Push `set variable [var] to (1 + 1)`
script.push_stack(b.StackBlock("data_setvariableto", {"VALUE": b.BlockInput(inner, False, default=b.ScratchValue(""))}, {"VARIABLE": [v.name, v.uid]}))
# Create substack
subs = b.SubStack()
# Create and push (1 + 1) block
inner2 = script.push_op(b.OpBlock("operator_add", {"NUM1": b.BlockInput(b.ScratchValue(1), True),"NUM2": b.BlockInput(b.ScratchValue(1), True)}, {}))
# inner = b.ScratchValue(2)
# Push `change variable [var] by (1+1)` to substack
subs.push_stack(b.StackBlock("data_changevariableby", {"VALUE": b.BlockInput(inner2, False)}, {"VARIABLE": [v.name, v.uid]}))
# Push the substack to the stage
stage.push_substack(subs)
# Push `forever {substack}` to the main script
script.push_stack(b.StackBlock("control_forever", {}, {}, substack=subs))
# Push the main script to the stage
stage.push_substack(script)

# Create procedure with an input named `test`
test = b.ProcedureInput("test")
proc = b.Procedure("example", [test])
# Create a variable named `variable`
v2 = stage.create_variable("variable", 0)
# Push `change variable [variable] by (1)` to procedure definition
proc.definition.push_stack(b.StackBlock("data_changevariableby", {"VALUE": b.BlockInput(b.ScratchValue(1), True)}, {"VARIABLE": [v2.name, v2.uid]}))
# Push `procedure example (variable)` to the procedure
proc.definition.push_stack(proc.call_proc({proc.arguments[0]: b.BlockInput(v2, False)}))
# Push this procedure to the stage
stage.push_proc(proc)

pf = p.ProjectFile([stage])
p.project_to_zip(pf, "example.sb3")
