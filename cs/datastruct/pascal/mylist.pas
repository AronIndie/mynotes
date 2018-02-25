{$mode objfpc} // directive to be used for defining classes
{$m+}		   // directive to be used for using constructor

program mylists;

type
   node	= Class
   public
   value : integer;
   next:^node;
   constructor create(i:integer);
end;

type
   mylist = class
   private
   length:integer;
   head : ^node;
   public
   constructor create();
   procedure get_length;
      procedure add(value : integer);
end;			  

constructor node.create(i :integer );
begin
   value = i;
end;

constructor mylist.create();
begin
   length:= 0;
end;

procedure mylist.add(value :integer);
var
   new_node,last_node	: node;
   count	: integer;
begin
   new_node := node.create(value);
   if length = 0 then
      head := @new_node
   else
      begin
	 count := length;
	 last_node := head^;
	 while count > 1 do
	    begin
	       last_node := last_node.next^;
	       count = count - 1;
	    end;
	 last_node.next := @new_node;
      end;
end;

procedure mylist.get_length();
begin
   writeln(length);
end;

var
   this_node : node;
   this_list : mylist;
   
   
begin
   this_node := node.create();
   this_list := mylist.create(this_node);
   this_list.get_length;
end.
