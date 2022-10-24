import { Component, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'app-tool-bar',
  templateUrl: './tool-bar.component.html',
  styleUrls: ['./tool-bar.component.scss'],
})
export class ToolBarComponent implements OnInit {
  @ViewChild('popover') popover;
  constructor() { }

  ngOnInit() {}

  hidePopover(e: Event) {
    this.popover.event = e;
    this.popover.dismiss().then(() => { this.popover = null; });
  }

}
