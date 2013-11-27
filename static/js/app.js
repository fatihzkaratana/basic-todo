/**
 * The MIT License (MIT)

 * Copyright (c) 2013 fatih

 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:

 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.

 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 * Created by fatih on 26/11/13.
 */

(function($){
    /**
     * Create a Datepicker
     */
    $('.datepicker').datepicker();
    var target = $("form.form-inline");

    /**
     * Bind status change event to the checkboxes
     */
    $('input[type="checkbox"]').change(function(){
        if ( $(this).val() == "Closed" && !$(this).checked) {
            $(this).val("Open");
        }else{
            $(this).val("Closed");
        }
    })

    /**
     * Bind remove event to the remove button
     */
    $('button.remove').click(function(){
        id = $(this).data("id");
        $.post("/remove",{id: id}, function(data){
            switch (data.code){
                case 200:
                    html = '<div class="alert alert-success"><b>Status '+ data.code + '</b><br>' + data.message + '</div>';
                    target.prepend(html).show("slow");
                    setTimeout(function(){
                        target.find(".alert").hide("slow").remove();
                        $("#" + id + ".row").hide("slow").remove();
                        $("#" + id + ".row hr").hide("slow").remove();
                    }, 4000);
                    break;
                case 500:
                    html = '<div class="alert alert-warning"><b>Status '+ data.code + '</b><br>' + data.message + '</div>';
                    target.prepend(html).show("slow");
                    setTimeout(function(){
                       target.find(".alert").hide("slow").remove();
                    }, 4000);
                    break;
                default:
                    html = '<div class="alert alert-warning"><b>Status '+ data.code + '</b><br>' + data.message + '</div>';
                    target.prepend(html).show("slow");
                    setTimeout(function(){
                       target.find(".alert").hide("slow").remove();
                    }, 4000);
                    break;
            }
        });
    });

    /**
     * Bind edit event to the remove button
     */
    $('button.edit').click(function(){
        id = $(this).data("id");
        $(this).html("Save");
        $(this).removeClass("edit").addClass("save").on("click", function(){
            $.editTask(id);
        });
        $(this).parent().parent().find("input, select").each(function(){
            $(this).removeAttr("disabled");
        });
    });

    /**
     * Edit task method has been implemented right here
     */
    $.editTask = function(id){
        var post_data = {};
        $("button.save").parent().parent().find("input, select").each(function(e){
            key = $(this).data("id").replace("-" + id, "");
            console.log(key);
            post_data[key] = $(this).val();
        });
        post_data["id"] = id;
        post_data["status"] = "Closed" ? $("#status-" + id).val() : "Open";

        $.post("/edit",post_data, function(data){
            switch (data.code){
                case 200:
                    html = '<div class="alert alert-success"><b>Status '+ data.code + '</b><br>' + data.message + '</div>';
                    target.prepend(html).show("slow");
                    $("#button-" + id).removeClass("save").addClass("edit").html("Edit").unbind("click");
                    $("#button-" + id).parent().parent().find("input, select").each(function(e){
                        $(this).attr("disabled","disabled");
                    });
                    setTimeout(function(){
                        target.find(".alert").hide("slow").remove();
                    }, 4000);
                    break;
                case 500:
                    html = '<div class="alert alert-warning"><b>Status '+ data.code + '</b><br>' + data.message + '</div>';
                    target.prepend(html).show("slow");
                    setTimeout(function(){
                       target.find(".alert").hide("slow").remove();
                    }, 4000);
                    break;
                default:
                    html = '<div class="alert alert-warning"><b>Status '+ data.code + '</b><br>' + data.message + '</div>';
                    target.prepend(html).show("slow");
                    setTimeout(function(){
                       target.find(".alert").hide("slow").remove();
                    }, 4000);
                    break;
            }
        });
    }

    /**
     * Bind add task event to the remove button
     */
    $('button.add').click(function(){
        id = $(this).data("id");

        /**
         * In that case I can use a Javascript templating engine such Mustache,
         * but recently ı do not need more dependency, all I have is enough.
         * @type {string}
         */
        var html = '<div class="row new">' +
                          '<div class="col-md-12">' +
                            '<div class="input-group">' +
                              '<span class="input-group-addon">' +
                                  '<input type="checkbox" name="status" value="Open">' +
                              '</span>' +
                              '<input type="text"  value="" name="value"  class="form-control">' +
                            '</div><!-- /input-group -->' +
                          '<div style="margin-top: 5px;" class="clearfix"></div>' +
                          '<div class="form-group">' +
                                '<input type="text" value="" class="form-control datepicker" name="due_date">' +
                          '</div>' +
                          '<div class="form-group">' +
                                '<select class="form-control" name="assignee">' +
                                            '<option value="Teunis Jaylen">Teunis Jaylen</option>' +
                                            '<option value="Samuel Engelbert">Samuel Engelbert</option>' +
                                            '<option value="Edvard Jancsi">Edvard Jancsi</option>' +
                                            '<option value="Fatih Karatana">Fatih Karatana</option>' +
                                '</select>' +
                            '</div>' +
                          '<div class="pull-right">' +
                              '<button class="save btn btn-sm btn-info" id="save" type="button">Save</button>' +
                              '<button class="cancel btn btn-sm btn-danger" type="button">Cancel</button>' +
                          '</div>' +
                          '</div><!-- /.col-lg-6 -->' +
                        '</div>' +
            '<hr class="clearfix" />';
        $(this).before(html);
        $('.datepicker').datepicker();
        $(".new").find("button#save").bind("click", function(){
            var post_data = {};
            $(this).parent().parent().find("input, select").each(function(e){
                key = $(this).attr("name");
                console.log(key);
                post_data[key] = $(this).val();
            });
            post_data["status"] = "Closed" ? $("#status-" + id).val() : "Open";

            $.post("/add",post_data, function(data){
                switch (data.code){
                    case 200:
                        html = '<div class="alert alert-success"><b>Status '+ data.code + '</b><br>' + data.message + '</div>';
                        target.prepend(html).show("slow");
                        setTimeout(function(){
                            window.location = "localhost:8000";
                        }, 4000);
                        break;
                    case 500:
                        html = '<div class="alert alert-warning"><b>Status '+ data.code + '</b><br>' + data.message + '</div>';
                        target.prepend(html).show("slow");
                        setTimeout(function(){
                           target.find(".alert").hide("slow").remove();
                        }, 4000);
                        break;
                    default:
                        html = '<div class="alert alert-warning"><b>Status '+ data.code + '</b><br>' + data.message + '</div>';
                        target.prepend(html).show("slow");
                        setTimeout(function(){
                           target.find(".alert").hide("slow").remove();
                        }, 4000);
                    break;
                }
            });
        });
    });
})(jQuery)
