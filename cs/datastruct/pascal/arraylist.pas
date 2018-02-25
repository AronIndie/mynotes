program array_list;

{$mode objfpc} // directive to be used for defining classes
{$m+}		   // directive to be used for using constructor

type
   arraylist = class
   private
      length : integer;
      default_capacity :integer;
      values : array[1..8] of integer;
   public
      procedure ensure_capacity(capacity : integer);
      // procedure add(value:integer);
      // procedure remove(i:integer);
      // function get_length():integer;
      // procedure myset(i, value:integer);
      // function get(i:integer):integer;
      // procedure insert(i, value:integer);
      // procedure print;
   end;

   procedure arraylist.ensure_capacity(capacity:integer);
   begin
      writeln('ensure_capacity');
   end;

var
    myarraylist : arraylist;
    capacity:integer = 9;
begin
   myarraylist := arraylist.Create;
   myarraylist.ensure_capacity(capacity);
end.

