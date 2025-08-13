Declaring variable of a given precision
```fortran
	integer, parameter :: dp = selected_real_kind(15,300)
	real(kind=dp) :: X, Y
	X = 6.0_dp
```
The variable will have at least 15 significant decimal places and could represent numbers from $10^{-300}$ to $10^{300}$.

Derived data types
```fortran
type particle
	real(dp) :: x
	real(dp) :: y
	real(dp) :: z
	real(dp) :: m
end type particle

type(particle) :: p0
p0 % x = 3.14
```
Array declarations
```fortran
real(dp), dimension(20,20) :: K
real(dp) :: fe(6)
```
Arrays with custom indices
```fotran
real(dp) :: idx(-3:3)

ubound(idx, dim=1, kind=requested_kind_of_bound) ! 3
lbound(idx, dim=1, kind=requested_kind_of_bound) ! -3
```
Assigning a certain value to a whole array
```fortran
K = 5.0_dp
```
Assigning many values with a single statement
```fortran
real(dp) :: v(5)
v = (/ 1.0_dp, 2.0_dp, 3.0_dp, 4.0_dp, 5.0_dp /)
```
Slicing for rows and columns in assignments
```fortran
K(5,:) ! row 5
K(:,4) ! column 4
```
Fortran stores arrays in memory **by column** (column-major order). NumPy arrays can be stored in the same way by specifying in the array constructor the option `pkeyw(order=F)`.

Allocatable arrays of different dimensions
```fortran
real, dimension(:,:), allocatable :: K
real, dimension(:), allocatable :: f

allocate(K(20,20))
allocate(f(20))

deallocate(K)
deallocate(f)
```
Allocatable arrays can also be dummy function arguments.
Allocatable functions:
```fortran
real, allocatable, dimension(:) :: A
A = create_vector(30)

function create_vector(n)
	real, allocatable, dimension(:) :: create_vector
	integer, intent(in) :: n
	allocate(create_vector(n))
end function
```
Note, there is:
```Fortran
intent(in)
intent(out)
intent(inout)
```
Syntax of the select statement
```fortran
select case (value)
	case (0:1)
		write(*,*) 'Less than one!'
	case (1)
		write(*,*) "One!"
	case (43:)
		write(*,*) 'More than the meaning of life'
	case default
		write(*,*) 'Something else'
end select 
```
While statement (there is also a range `do`)
```fortren
do while x < 1.05
	f = sin(x)
	x = x + 0.1
	write(*,*) x. f
end do
```
Embarrassingly parallel calculations:
```Fortran
do concurrent (i = 1:grid_size)
	h(i) = exp(-decay * (i - icenter)**2)
end do
```
#### Useful intrinsic functions
###### Mathematical
```fortran
dot_product(u, v)
matmul(A, B)
transpose(C)

all(mask)
any(mask)
count(mask)

maxval(array)
minval(array)
product(array)
sum(array)
size(array)
```
###### Arrays and matrices:
```Fortran
rank(arr)
shape(arr)
size(arr)
matrix = reshape(array, shape=[3,3], order=[2,1],pad=padding_array)
```
Default pad is `[1,2]` which is row-major
```Fortran
matrt = transpose(matr)
matr2 = eoshift(matr, shift=-1, boundsry=42, dim=2)
matr2 = cshift(matr, shift=-1, dim=2)
```
Positive `shift` - to the right, negative, to the left, `dim=1` - column, `2` - row.
```Fortran
all(M > 0, dim=1)
any(M > 0, dim=1)
count(M > 0, dim=1)
maxval(M, dim=1, M < 0)
minval(M, dim=1, M < 0)
sum(M, dim=1, M < 0)
maxloc(M, M < 0)
minloc(M, M < 0)
product(M, dim=1, M < 0)
merge(matr1, matr2, matr1 > 0)
pack(M, M > 0)
spread(arr, dim=2, ncopies=40)
dotproduct(arr1, arr2)
matmul(matr1, matr2)
```
##### String
```
str = trim(str)
```
###### Navigating in a (scratch) file
```Fortran
rewind()
backspace()
```
#### Modular programming
Subroutines
```fortran
subroutine myproc(a, B, C)
	implicit none
	integer :: a
	real, dimension(a, *) :: B
	real, dimension(a) :: C
	! ...
	return
end subroutine

call myproc(d, E, F)
```
Functions
```fortran
real function f(x) result(res)
	real :: x, res
	res=sin(x)
end function f

a = f(y)
```
Naming result variable:
```Fortran
real function f(x)
	real :: x
	f=sin(x)
	return
end function f
```
Stating the function type in the declaration block:
```Fortran
program main
	implicit none
	integer(kind=1) :: cube, num
	num = 2
	num = cube(num)
end program

function cube(num)
	cube = num ** 3
end function
```
Pure functions (do not allow side effects):
```Fortran
pure integer function sum(a, b)
	integer, intent(in) :: a, b
	sum = a + b
end function sum
```
Elemental functions (can work both on single elements and on arrays):
```Fortran
elemental integer function sum(a, b)
	integer, intent(in) :: a, b
	sum = a + b
end function sum
```
They are by default `pure`. Since Fortran 2014 one can declare `impure elemental` functions.
Recursive subroutines must be declared as such:
```Fortran
recursive integer function fib(n) ...
```
Optional and keyword arguments
```fortran
subroutine order_icecream(number, flavor, topping)
	integer :: number
	integer, optional :: flavor
	integer, optional :: topping

	print *, number, 'icecreams ordered'
	if (present(topping)) then
		print *, 'topping is', topping
	else
		print *, 'no topping is given'
	end if
	if (present(flavor)) then
		print *, 'flavor is', flavor
	else
		print *, 'no flavor is given'
	end if
end subroutine

call order_icecream(3, topping=3)
```
Higher order functions
```fortran
real function integrate(a, b, func)
	real :: a, b
	interface
		real function func(x)
			real, intent(in) ::
		end function func
	end interface
	!...
end function integrate

real function myfunc(x)
	real :: x
	myfunc = sin(x)**2
end funcion myfunc

area.= integrate(1.0, 2.0, myfunc)
```
###### Modules
Modules are created in a similar way as main programs, but with `module` keyword. Their variable can have `public` and `private` attributes. Subroutines and functions can be declared as `private` before the `contains` block:
```fortran
module mymodule
	private mysub
contains
	subroutine mysum
	!...
	end subroutine
end module mymodule
```
Importing (might be in a block)
```Fortran
use mymodule
use mymodule only: mysum
```
Function overloading
```fortran
module overloaded
	interface func
		module procedure ifunc, rfunc
	end interface
contains
	integer function ifunc(x)
		integer, intent(in) :: x
		ifunc = x * 42
	end function ifunc
	real function rfunc(x)
		real, intent(in) :: x
		rfunc = x / 42.0
	end function rfunc
end module overloaded

integer :: a = 42
real :: b = 42.0

c = func(a)
d = func(b)
```
Operators can also be overloaded
```fortran
module vector_ops
	interface operator(+)
		module procedure vector_plus_op
	end interface
	
end module vector_ops
```
###### File I/O
Checking if a file exists:
```Fortran
inquire(filename, exists=exists_variable)
```
```fortran
integer, parameter :: infile = 15
integer, parameter :: outfile = 16

open(unit=infile, file='indata.dat',access='sequential',action='read')
open(unit=outfile, file='outdata.dat',access='sequential',action='out')
open(newunit=newunit_variable, file='outdata.dat',status='new')
open(newunit=newunit_variable, file='outdata.dat',status='old',position='append',iostat=iostat_var)
open(newunit=newunit_variable,status='scratch',position='append',iostat=iostat_var)
```
When `iostat_var` is `0`, there was no error.
Unit numbers can be used in `read` and `write` statements. 
```Fortran
write(unit=unit, fmt=fmt, advance="no"), string_to_write
```
If `advance="no"`, no new line will be added
The files should be closed:
```fortran
close(infile)
close(outfile)
```
One can also use strings instead of file units. This technique can be used to make up formst specifiers for dynamic printing.
Defining namelists
```fortran
integer :: no_of_eggs, litres_of_milk, kilos_of_butter, list(5)
namelist /food/ no_of_eggs, litres_of_milk, kilos_of_butter, list
read (ir, nml=food)
write(ir, nml=food)
```
Unformatted (binary) I/O
```fortran
open(unit=ir, file='arrays.dat', form='unformatted')
read(ir) A
```
Direct access files store equally spaced records and allows random access to them.
```fortran
type account
    character(len=40) :: account_holder
    real :: balance
end type account

type(account) :: account
integer :: recordSize
!...
inquire(iolength=recordSize) account
!...
open(unit=iw, file='accounts.dat', access='direct', recl=recordSize, status='replace')
write(iw, rec=1) account
```
Error handling in I/O operations
```fortran
	open(unit=ir, file='test.txt', status='old', err=101)
	read(ir,*,err=102,iostat=ierr) a
	stop
101 print *, 'An error occured when opening the file.'
	stop
102 print *, 'An error occured when reading the file.'
	stop
```
Or simpler:
```Fortran
	open(unit=ir, file='test.txt', status='old', err=101)
	read(ir,*,err=102,iostat=ierr) a
	stop
101 stop 'An error occured when opening the file.'
102 stop 'An error occured when reading the file.'

```
The variable `iostat` will contain error code or 0.

New `forall` statements to replace nested loops
```fortran
forall(i=1:n, j=1:m)
    A(i,j)=i+j
end forall
```
New `where` statement for simpler matrix operations
```fortran
where (A>1)
    B = 0
else where
    B = A
end where
```
#### Pointers
```fortran
integer, allocatable, dimension(:,:), target :: A
integer, dimension(:,:), pointer :: B, C

allocate(A(20,20))

if (allocate(A)) then
! ...
end if

B => A
B => null()

```
#### Object-oriented programming
```fortran
module particles
	type particle_class
	private
		real :: m_pos(3)
		real :: m_vel(3)
	contains
		procedure :: init => particle_init
		procedure :: set_position => particle_set_position
		procedure :: set_velocity => particle_set_velocity
		procedure :: get_position => particle_get_position
	    procedure :: get_velocity => particle_get_velocity
	    procedure, private :: setup => particle_setup
	end type particle_class

	type, extends(particle_class) :: sphere_particle_class
	private
	    real :: m_radius
	contains
	    procedure :: set_radius => sphere_set_radius
	    procedure :: get_radius => sphere_get_radius
	end type sphere_particle_class

contains
	subroutine particle_init(this)
		class(particle_class) :: this
		this % m_pos = (/0.0, 0.0, 0.0/)		
		this % m_vel = (/0.0, 0.0, 0.0/)
	end subroutine particle_init

	subroutine particle_set_position(this, x, y ,z)
		class(particle_class) :: this
	    real :: x, y, z
	    this % m_pos = (/x, y, z/)
	end subroutine particle_set_position

	subroutine particle_set_velocity(this, vx, vy ,vz)
		class(particle_class) :: this
	    real :: vx, vy, vz
	    this % m_vel = (/vx, vy, vz/)
	end subroutine particle_set_velocity

	subroutine particle_get_position(this, x, y ,z)
		class(particle_class) :: this
	    real, intent(out) :: x, y, z
	    x = this % m_pos(1)
	    y = this % m_pos(2)
	    z = this % m_pos(3)
	end subroutine particle_get_position

	subroutine particle_get_velocity(this, vx, vy ,vz)
	    class(particle_class) :: this
	    real, intent(out) :: vx, vy, vz
	    vx = this % m_vel(1)
	    vy = this % m_vel(2)
	    vz = this % m_vel(3)
	end subroutine particle_get_velocity

end module particles
!...
real :: vx, vy, vz
!...
type(particle_class) :: particle
call particle % init
call particle % set_position(1.0, 1.0, 1.0)
call particle % get_velocity(vx, vy, vz)
```
Calling an inherited method
```fortran
call this % particle_class % init()
```