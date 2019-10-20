import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {HomeComponent} from "./home/home.component";
import {MatchesComponent} from "./matches/matches.component";
import {SignUpComponent} from "./sign-up/sign-up.component";


const routes: Routes = [{
  path: "",
  component: HomeComponent,
  pathMatch: "full"
}, {
  path: "matches",
  component: MatchesComponent
}, {
  path: "sign_up",
  component: SignUpComponent
}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
