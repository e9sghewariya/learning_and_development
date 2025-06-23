
-->Checkboxes and radio button:

Understood how to add and group checkboxes using `form-check` class.
Learned to use `form-check-input` for inputs and `form-check-label` for labels.

Example:
<html>
  <div class="form-check">
    <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
    <label class="form-check-label" for="defaultCheck1">
      Default checkbox
    </label>
  </div>
</html>

Similar structure applies to radio buttons.
Example:
<html>
  <div class="form-check">
    <input class="form-check-input" type="radio" name="radioDefault" id="radioDefault1">
    <label class="form-check-label" for="radioDefault1">
      Default Radiobutton
    </label>
  </div>
</html>


-->Dropdowns

Explored Bootstrap’s dropdown component using dropdown class.
Realized we can nest dropdowns in navbars, buttons, or as standalone.

Example:

<div class="dropdown">
    <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown">
        Dropdown button
    </button>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">Action</a></li>
    </ul>
</div>

-->Scrolling (Horizontal & Vertical)
  Used overflow-auto, overflow-scroll, and specific widths/heights.
  Tested with long text/table divs.
    Example:
    <div style="height: 200px;" class="overflow-auto">
      <!-- content here -->
    </div>

-->Collapsible Content
    Explored about how to  collapse component.
    Used it for toggling sections on click.
    Example:

<a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample">
      Toggle
</a>
 <div class="collapse" id="collapseExample">
    <div class="card card-body">
     Collapsed content here
    </div>
</div>

-->Grids and Layouts

    Learned about rows and columns using .row and .col-md-* classes.
    Checked how to align and position elements using Bootstrap’s grid system.
    Also used spacing utilities like p-*, m-*, and gap-*.

-->Extending HTML & CSS Basics
    Understood how to extend an HTML file using Django’s {% extends %} and {% block content %}.
    Refreshed CSS basics like:
        -->display, position, margin, padding, border
        -->inline vs block elements
        -->class selectors and id selectors
